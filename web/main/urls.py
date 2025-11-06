from django.contrib import admin
from django.urls import path

from tasks import views


def tie(ruta, vista, name=None):
    return path(ruta, vista, name=name or vista.__name__)


urlpatterns = [
    tie('', views.homepage),
    path("admin/", admin.site.urls),
]
