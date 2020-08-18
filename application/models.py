from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    image = models.ImageField(upload_to = 'images/')

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()


class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
