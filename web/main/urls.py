from django.contrib import admin
from django.urls import path

from tasks import views


def tie(ruta, vista, name=None):
    return path(ruta, vista, name=name or vista.__name__)


urlpatterns = [
    tie('', views.homepage),
    tie('add/', views.add_task),
    tie('task/<int:id_task>/', views.view_task),
    tie('task/<int:id_task>/edit/', views.edit_task),
    path("admin/", admin.site.urls),
]
