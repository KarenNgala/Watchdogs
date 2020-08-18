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
