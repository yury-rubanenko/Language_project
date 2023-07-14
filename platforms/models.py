from django.db import models

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
