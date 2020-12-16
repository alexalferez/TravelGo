from django.db import models
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(
        max_length=2,
        choices=CITIES,
        default=CITIES[0][0]
    )
    description = description = models.TextField(max_length=250)
    def __str__(self):
        return self.name