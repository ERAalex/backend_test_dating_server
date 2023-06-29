from django.urls import include, path
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path("users/", include(router.urls)),

]
