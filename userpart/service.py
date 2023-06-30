from django_filters import filters
import django_filters
from .models import UserAccount


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserFilter(django_filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    surname = CharFilterInFilter(field_name='surname', lookup_expr='in')
    sex = CharFilterInFilter(field_name='sex', lookup_expr='in')

    class Meta:
        model = UserAccount
        fields = ['name', 'surname', 'sex', ]
