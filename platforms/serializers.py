from rest_framework import serializers
from .models import UserWord, Word


class UserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = ('__all__')

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('__all__')
