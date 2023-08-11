from rest_framework import serializers
from .models import UserWord, Word


class UserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = ('word', 'user', 'learned_at')

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'picture', 'translation', 'transcription', 'language')
