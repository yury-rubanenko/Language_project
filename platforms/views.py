from django_filters.rest_framework import DjangoFilterBackend
from .models import UserWord, Word
from .serializers import UserWordSerializer, WordSerializer, CreateUserWordSerializer, UpdateUserWordSerializer, DeleteUserWordSerializer
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from .filter import UserWordFilter
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

# list all words(GET)
class WordListView(ListAPIView):
    serializer_class = WordSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        language = self.kwargs['language_slag']
        if language not in Word.LanguageChoices:
            raise NotFound()
        
        return Word.objects.all()
    
# user words list (POST-GET)
class UserWordsListView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserWordFilter

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return CreateUserWordSerializer
        else:
            return UserWordSerializer
        
    def get_queryset(self):
        language = self.kwargs['language_slag']
        if language not in Word.LanguageChoices:
            raise NotFound()
        
        return UserWord.objects.filter(word__language=language, user=self.request.user).select_related('word')
    
# user word (PATCH)
class UpdateUserWordsAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserWordFilter
    serializer_class = UpdateUserWordSerializer

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

# user word (DELETE)
class DeleteUserWordsAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserWordFilter
    serializer_class = DeleteUserWordSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    