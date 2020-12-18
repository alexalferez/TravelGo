from django.forms import ModelForm
from .models import Recommendation, Profile

class RecommendationForm(ModelForm):
  class Meta:
    model = Recommendation
    fields = ['name', 'city', 'description']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['name','user','city','description']