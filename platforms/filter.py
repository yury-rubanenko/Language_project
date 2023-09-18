import django_filters
from django.forms.widgets import DateInput
from django.db.models import Count

from .models import UserWord, Word


class UserWordFilter(django_filters.FilterSet):
    learned_at = django_filters.DateFilter(
        field_name="learned_at", lookup_expr="gte", widget=DateInput(attrs={"type": "date"})
    )
    learned_at__lte = django_filters.DateFilter(
        field_name="learned_at", lookup_expr="lte", widget=DateInput(attrs={"type": "date"})
    )
    not_learned = django_filters.BooleanFilter(
        field_name="learned_at", lookup_expr="isnull", exclude=True
    )

    class Meta:
        model = UserWord
        fields = []



class WordFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(method="filter_tags")

    class Meta:
        model = Word
        fields = []

    def filter_tags(self, queryset, name, value):
        tags = value.split(',')
        return queryset.filter(tags__name__in=tags)
