from django.forms import ModelForm
from .models import Recommendation, Profile, Comment

class RecommendationForm(ModelForm):
  class Meta:
    model = Recommendation
    fields = ['name', 'city', 'description']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['name','user','city','description']

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']