from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexCapturas, name="indexcapturas"),
    path("editar/<int:id>", views.editarCaptura, name="editarcaptura"),
] 