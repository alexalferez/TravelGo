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
    description = description = models.TextField(max_length=250)
    # add recommendations field

    def __str__(self):
        return self.name

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
    # def get_absolute_url(self):
    #     return reverse('detail', kawrgs={'recommendation_id': self.id})

    
    ## Add photo class for photo model