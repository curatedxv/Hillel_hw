from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ratings(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authot')
    recipient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipient')
    rating = models.IntegerField()
    text = models.TextField()