from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indexpublicacion"),
    path("like/", views.likePublicacion, name="likepublicacion")
]