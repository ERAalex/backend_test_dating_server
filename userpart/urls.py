from django.urls import include, path
from rest_framework import routers
from .views import create_user


urlpatterns = [
    path("api/clients/create", create_user),
]
