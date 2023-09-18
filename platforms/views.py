from django.db.models import Avg, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.generics import DestroyAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .filter import UserWordFilter, WordFilter
from .models import UserWord, Word
from .serializers import (
    CreateUserWordSerializer,
    DeleteUserWordSerializer,
    UpdateUserWordSerializer,
    UserWordSerializer,
    WordSerializer,
)


class TagStatisticsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tag_counts = Word.objects.values("language").annotate(total_tags=Count("tags"))
        total_tags = Word.objects.aggregate(total=Count("tags"))["total"]
        average_number = Word.objects.annotate(tags_count=Count("tags")).aggregate(
            average=Avg("tags_count")
        )["average"]

        data = {
            "tag_counts_per_language": tag_counts,
            "total_tags": total_tags,
            "average_number_tag": average_number,
        }
        return Response(data)


class WordPagination(PageNumberPagination):
    page_size = 15


# list all words(GET)
class WordListView(ListAPIView):
    serializer_class = WordSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = WordPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WordFilter

    def get_queryset(self):
        language = self.kwargs["language_slag"]
        if language not in Word.LanguageChoices:
            raise NotFound()

        queryset = Word.objects.all()
        return queryset

# user words list (POST-GET)
class UserWordsListView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserWordFilter

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CreateUserWordSerializer
        else:
            return UserWordSerializer

    def get_queryset(self):
        language = self.kwargs["language_slag"]
        if language not in Word.LanguageChoices:
            raise NotFound()

        return UserWord.objects.filter(
            word__language=language, user=self.request.user
        ).select_related("word")


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
