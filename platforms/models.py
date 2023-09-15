from django.db import models

from profiles.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Word(models.Model):
    class LanguageChoices(models.TextChoices):
        ENGLISH = "en"
        UKRAINIAN = "ua"

    word = models.CharField(max_length=128)
    picture = models.ImageField(upload_to="images/", max_length=255, blank=True)
    translation = models.CharField(max_length=128)
    transcription = models.CharField(max_length=128, blank=True)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    tags = models.ManyToManyField(Tag, blank=True, related_name="words")

    def __str__(self):
        return self.word


class UserWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="users_words")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_words")
    learned_at = models.DateField(null=True, blank=True)
