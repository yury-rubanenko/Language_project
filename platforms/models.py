from django.db import models
from profiles.models import User
# Create your models here.


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('UA', 'Ukrainian'),
        ('EN', 'English'),
    ]

    name = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.get_name_display()


class Word(models.Model):
    word = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='images/', max_length=255)
    translation = models.CharField(max_length=128)
    transcription = models.CharField(max_length=128, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE) 

    def __str__(self):
        return self.word

class UsersWords(models.Model):
    user_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='users_words')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_words')
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name.username} - {self.user_word.word}"