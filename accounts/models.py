from django.db import models
from django.contrib.auth.models import User
from datetime import date,timedelta
from django.utils import timezone, timesince
# Create your models here.

class UserProfile(models.Model):
    gender = (
        ("f","Female"),
        ("m","Male"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=gender, blank=True, null=True)
    dob = models.DateField(blank=True,null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    contact = models.CharField(max_length=20,blank=True,null=True)

    def age_func(self):
        self.age = (timezone.now() - self.dob).year()

    def __str__(self):
        return f"{self.user.username}"

