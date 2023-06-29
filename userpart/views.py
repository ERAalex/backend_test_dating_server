from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from .serializers import UserCreateSerializer



@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    """Создание пользователя через отдельный  endpoint. В Djoser уже готова эта логика, оставил по ТЗ"""

    serializer = UserCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
