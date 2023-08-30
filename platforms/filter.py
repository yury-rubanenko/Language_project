from django import forms
import django_filters
from django_filters import rest_framework as filters
from django.forms.widgets import DateInput
from .models import UserWord


class UserWordFilter(django_filters.FilterSet):
    learned_at = django_filters.DateFilter(
        field_name='learned_at',
        lookup_expr='gte',
        widget=DateInput(attrs={'type': 'date'})
    )
    learned_at__lte = django_filters.DateFilter(
        field_name='learned_at',
        lookup_expr='lte',
        widget=DateInput(attrs={'type': 'date'})
    )
    not_learned = django_filters.BooleanFilter(
        field_name='learned_at',
        lookup_expr='isnull',
        exclude=True
    )
    class Meta:
        model = UserWord
        fields = []

