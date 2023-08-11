from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserWord, Word
from .serializers import UserWordSerializer, WordSerializer
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter


class UserWordsListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserWordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['learned_at']
    search_fields = ['word__word', 'word__translation']
    ordering_fields = ['learned_at']

    def get_queryset(self):
        user = self.request.user
        queryset = UserWord.objects.filter(user=user)

        status = self.request.query_params.get('status', None)
        if status == 'learned':
            queryset = queryset.exclude(learned_at=None)
        elif status == 'unlearned':
            queryset = queryset.filter(learned_at=None)
        return queryset
    

class WordListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
    permission_classes = [permissions.AllowAny]
