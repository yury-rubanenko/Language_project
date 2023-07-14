from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=2, choices=...)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=128)
    picture = models.ImageField(max_length=...)
    translation = models.CharField(max_length=128)
    transcription = models.CharField(max_length=128)
    language = models.ForeignKey(Language, on_delete=models.CASCADE) 

    def __str__(self):
        return self.word
