from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import UserWord, Word
from .serializers import UserWordSerializer, WordSerializer

class UserWordsListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserWordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status = self.request.query_params.get('status', None)

        if status == 'learned':
            queryset = UserWord.objects.filter(user=user, learned_at__isnull=False)
        elif status == 'unlearned':
            queryset = UserWord.objects.filter(user=user, learned_at__isnull=True)
        else:
            queryset = UserWord.objects.filter(user=user)

        return queryset

class WordListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
    permission_classes = [permissions.AllowAny]


