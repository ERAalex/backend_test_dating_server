from django.urls import path
from .views import create_user, make_match, UsersListView


urlpatterns = [
    path("api/clients/create", create_user),
    path("api/<int:match>/match", make_match),
    path("api/list", UsersListView.as_view()),
]
