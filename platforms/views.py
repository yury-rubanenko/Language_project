from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserWord, Word
from .serializers import UserWordSerializer, WordSerializer
from rest_framework import permissions
from .filter import UserWordFilter


class UserWordsListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserWordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserWordFilter
    
    queryset = UserWord.objects.all() 


class WordListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
    permission_classes = [permissions.AllowAny]
