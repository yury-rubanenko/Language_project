from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True, unique=True)


    
    def __str__(self):
        return self.username

