from django.urls import path
from .views import create_user


urlpatterns = [
    path("api/clients/create", create_user),
]
