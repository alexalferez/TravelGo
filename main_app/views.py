from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recommendation, Photo, CITIES, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecommendationForm, CommentForm
# from django.shortcuts import get_object_or_404
# photo imports below
import uuid
import boto3


# Create your views here.
from django.http import HttpResponse

#Photo Constants
S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/' # base url
BUCKET = 'travelgo' # bucket name

# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_create')
    else:
      error_message = "Invalid sign up - try again"
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecommendationCreate(LoginRequiredMixin, CreateView):
  model = Recommendation
  fields = ['name', 'city','description']
  # assigns the user (self.request.user)
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecommendationUpdate(UpdateView):
  model = Recommendation
  fields = ['name', 'city','description']

class RecommendationDelete(DeleteView):
  model = Recommendation
  success_url = '/'

def home(request):
  recommendations = Recommendation.objects.all()
  return render(request, 'home.html', { 'recommendations': recommendations })

def about(request):
    return render(request, 'about.html')

def recommendations_detail(request, recommendation_id):
  recommendation = Recommendation.objects.get(id=recommendation_id)

  print(recommendation.__dict__, "name of town")
  return render(request, './recommendations/detail.html', { 'recommendation': recommendation})

  

class ProfileList(ListView):
  model = Profile

class ProfileDetail(DetailView):
  model = Profile
  

class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['name','city','description']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['name', 'city','description']

class ProfileDelete(DeleteView):
  model = Profile
  success_url = ''

def add_comment(request,recommendation_id):
  form = CommentForm(request.POST)
  user = Recommendation.objects.get(id=recommendation_id).user
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.user = user
    new_comment.recommendation_id = recommendation_id
    new_comment.save()
  return redirect('detail', recommendation_id=recommendation_id)

def add_photo(request, recommendation_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to recommendation_id or recommendation (if you have a recommendation object)
            Photo.objects.create(url=url, recommendation_id=recommendation_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', recommendation_id=recommendation_id)


class RecommendationCityList(ListView):
  
  template_name = 'recommendations/recommendation_city.html'
  def get_queryset(self):
    print(self.kwargs['city'], "self.kwargs['city']<------------------")
    #Loop through cities comparing their lowercase no space to city
    for c in CITIES:
      if self.kwargs['city'] == c[1].lower().replace(" ", ""):
        print(self.kwargs['city'], "city kwarg <---------===")
        self.kwargs['city'] = c[0]
        return Recommendation.objects.filter(city=self.kwargs['city'])
      else:
        error_message = "Invalid URL(404)"

      
    # self.city = get_object_or_404(Recommendation, city=self.kwargs['city'])
    # print(self.city, "<---------------- self.city")
    
  def get_context_data(self, **kwargs):
      # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in the publisher
    context['city'] = self.kwargs['city']
    print(context, "context <----------------")
    return context