from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexLogros, name="indexlogros"),
    path("editar/<int:id>", views.editarLogro, name="editarlogro"),
    path("publicar/", views.publicarLogro, name="publicarlogro"),
    path("nopublicar/", views.nopublicarLogro, name="nopublicarlogro"),
    path("borrar/<int:id>", views.borrarLogro, name="borrarlogro"),
    
]