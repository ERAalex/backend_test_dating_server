from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserAccountSerializer
from .models import UserRelations
from .tasks import confirmation_relation_email_celery
from .models import UserAccount

from django_filters import rest_framework as filters
from .service import UserFilter


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    """Создание пользователя через отдельный  endpoint. В Djoser уже готова эта логика, сделал этот эндпоинт по ТЗ"""

    serializer = UserAccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        # сюда логика нужно добавить штамп картинке
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def make_match(request, match):
    """ Проверяем связь с пользователем, отправляем письмо"""
    user = request.user.id

    check_match = UserRelations.objects.get(user=match)
    user_data = UserRelations.objects.get(user=user)
    # проверяем если мы уже находимся в понравившихся людях у интересующего нас пользователя
    if user in [item.id for item in check_match.match_persons.all()]:
        # проверяем если пользователь уже у нас в "любимых" и мы уже отправляли ему письмо
        if match in [item.id for item in user_data.liked_persons.all()] and match in \
                [item.id for item in user_data.match_persons.all()]:
            return Response('Между Вами уже есть любовная связь. Письмо уже ранее было отправлено')
        else:
            user_data.match_persons.add(match)
            user_data.liked_persons.add(match)

            ''' Обычная отправка письма - если не нужен сelery:'''
            # confirmation_relation_email(user_email=request.user.email, user_name=request.user.name,
            #                             user_match_email=check_match.user.email)

            ''' Celery - отправляем письмо'''
            confirmation_relation_email_celery.delay(user_email=request.user.email,
                                                     user_name=request.user.name,
                                                     user_match_email=check_match.user.email)

            return Response('письмо отправлено')

    user_data.match_persons.add(match)
    return Response('пользователь добавлен')


class UsersListView(generics.ListAPIView):
    """ Вывод списка пользователей """
    serializer_class = UserAccountSerializer
    permission_classes = [AllowAny, ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def get_queryset(self):
        users_data = UserAccount.objects.all()
        return users_data
