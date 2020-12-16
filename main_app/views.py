from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recommendation

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

class RecommendationCreate(CreateView):
  model = Recommendation
  fields = ['name', 'user', 'city','discrpition']

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
  return render(request, 'recommendations/detail.html')

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

