from django_filters import filters
import django_filters
from .models import UserAccount



def dist_between_two_lat_lon(*args):
    from math import asin, cos, radians, sin, sqrt
    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1)
    dist_longs = abs(long2 - long1)
    a = sin(dist_lats / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
    c = asin(sqrt(a)) * 2
    radius_earth = 6378  # the "Earth radius" R varies from 6356.752 km at the poles to 6378.137 km at the equator.
    return c * radius_earth


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserFilter(django_filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    surname = CharFilterInFilter(field_name='surname', lookup_expr='in')
    sex = CharFilterInFilter(field_name='sex', lookup_expr='in')
    # distance = django_filters.NumberFilter(field_name='distance', method='find_closest_lat_lon')
    distance = django_filters.NumberFilter(label='Введите дистанцию поиска', method='find_closest_lat_lon')
    def find_closest_lat_lon(self, queryset, name, value):

        data_users = queryset.all()
        user_latitude = self.request.user.latitude
        user_longitude = self.request.user.longitude

        # пробегаемся по пользователям и сохраняем тех кто по формуле выдает расстояние ближе заданного
        near_by_user = []
        for item in data_users:
            distance = dist_between_two_lat_lon(user_latitude, item.latitude, user_longitude, item.longitude)
            if distance <= value:
                near_by_user.append(item.email)
        if not value:
            return queryset.all()
        # выдаем тех, кого нашли и записали кроме самого пользователя. На будущее можно добавлять еще сколько км
        near_by_user.remove(self.request.user.email)
        return queryset.filter(email__in=near_by_user)

    class Meta:
        model = UserAccount
        fields = ['name', 'surname', 'sex', 'distance']
