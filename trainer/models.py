from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class TrainerDescriptions(models.Model):
    text = models.TextField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

class TrainerSchedule(models.Model):
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

class Services(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    level = models.IntegerField()
    duration = models.IntegerField()