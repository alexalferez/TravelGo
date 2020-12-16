from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recommendation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecommendationForm

# Create your views here.
from django.http import HttpResponse

# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = "Invalid sign up - try again"
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecommendationCreate(LoginRequiredMixin, CreateView):
  model = Recommendation
  fields = ['name', 'user', 'city','description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecommendationUpdate(UpdateView):
  model = Recommendation
  fields = ['name', 'city','discrpition']

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
  return render(request, './recommendations/detail.html')

class ProfileList(ListView):
  model = Profile

class ProfileDetail(DetailView):
  model = Profile

class ProfileCreate(CreateView):
  model = Profile

class ProfileUpdate(UpdateView):
  model = Profile

class ProfileDelete(DeleteView):
  model = Profile


def add_recommendation(request):
  form = RecommendationForm(request.POST)

  if form.is_valid():
    new_recommendation = form.save(commit=False)
    new_recommendation.user_id = user_id
    print(new_recommendation, "<----- new_rec")
    new_recommendation.save()
  return redirect('detail')

