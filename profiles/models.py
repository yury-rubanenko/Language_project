from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user = models.CharField(max_length=128)
    email = models.EmailField() 
    
    def __str__(self):
        return self.username