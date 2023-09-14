from rest_framework import serializers

from .models import UserWord, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word', 'picture', 'translation', 'transcription', 'language')
        read_only = ('id', )

class UserWordSerializer(serializers.ModelSerializer):
    word = WordSerializer(many=False)
    class Meta:
        model = UserWord
        fields = ('id', 'word', 'user', 'learned_at')
        read_only = ('id', 'word' )


class CreateUserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = ('word', 'user', 'learned_at')


class UpdateUserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = ['learned_at']


class DeleteUserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = ('word', 'user', 'learned_at')
