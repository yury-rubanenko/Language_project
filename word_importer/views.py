from platforms.serializers import WordSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from platforms.models import Word


class WordImportView(CreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer