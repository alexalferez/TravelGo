from django.contrib import admin
from .models import Profile, Recommendation, Photo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Recommendation)
admin.site.register(Photo)