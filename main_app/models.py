from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
CITIES = (
    ('LA', 'Los Angeles'),
    ('SF', 'San Francisco'),
    ('P', 'Portland'),
    ('S', 'Seattle')
)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(
        max_length=2,
        choices=CITIES,
        default=CITIES[0][0]
    )
    description = models.TextField(max_length=250)
    #do we need a recommendations section?

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.id})

## for the form, we only need to get the location_name, city, description and date_posted
## and photo after the photo model is added.
class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(
        max_length=2,
        choices=CITIES,
        default=CITIES[0][0]
    )
    description = models.TextField(max_length=250)
    # add photos field
    date_posted = date.today()

    def __str__(self):
        return self.name

    #we will add this when the recommendation detail route is set up. might need to change the
    #'detail' part depending on the route
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recommendation_id': self.id})

    def get_city_url(self):
        return self.get_city_display().lower().replace(" ", "")
        

    
## Add photo class for photo model
class Photo(models.Model):
    url = models.CharField(max_length=200)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for recommendation_id: {self.recommendation_id} @{self.url}"

class Comment(models.Model):
    date = date.today()
    comment = models.TextField(max_length=250)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"comment for {self.recommendation} by {self.user} on {self.date}"

    # class Meta:
    #     ordering = ['-date']quit