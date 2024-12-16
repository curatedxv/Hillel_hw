from django.db import models
from django.db import models
from django.contrib.auth.models import User
from trainer.models import Services
from trainer.models import Services


# Create your models here.

class Booking(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    trainer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainer")
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    service = models.ForeignKey(Services , on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
