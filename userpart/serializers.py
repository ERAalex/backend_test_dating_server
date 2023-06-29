from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser

from .models import UserAccount

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    """we need to use MultiPartParses for saving images"""
    parser_classes = (MultiPartParser,)

    class Meta:
        model = UserAccount
        fields = ("id", "email", "name", "password", "surname", "avatar", "sex")
