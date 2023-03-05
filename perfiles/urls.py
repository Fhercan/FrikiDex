from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indexperfiles"),
    path("editar/", views.editarPerfil, name="editarperfil")
]