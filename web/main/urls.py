from django.contrib import admin
from django.urls import path

from tasks import views


def tie(ruta, vista, name=None):
    return path(ruta, vista, name=name or vista.__name__)


urlpatterns = [
    tie('', views.homepage),
    tie('nueva/', views.add_task),
    tie('tarea/<slug:slu', views.add_task),
    path("admin/", admin.site.urls),
]
