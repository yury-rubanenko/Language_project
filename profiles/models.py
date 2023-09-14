from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    words = models.ManyToManyField("platforms.Word", through='platforms.UserWord', related_name='words')

    
    def __str__(self):
        return self.username

