from django.urls import path, re_path
from django.conf.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="Espinosa Alex - Dating Web Server",
        default_version="1v",
        description="API project description",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
