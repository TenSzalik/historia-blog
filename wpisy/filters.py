import django_filters
from django_filters import CharFilter
from django.db.models import Q

from .models import *

class EntryFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter',label="Search")

    class Meta:
        model = Entry
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Entry.objects.filter(
            Q(title__icontains=value) | Q(description__icontains=value) | Q(subtitle__icontains=value)
        )