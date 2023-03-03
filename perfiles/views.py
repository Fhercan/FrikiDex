from django.shortcuts import render
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil
# Create your views here.

@receiver(user_signed_up)
def createPerfil(sender=User, **kwargs):
    new_username = kwargs['user']
    user = User.objects.get(username = new_username)
    #Crear el perfil del usuario
    perfil=Perfil()
    perfil.user=user
    perfil.nombre=user.username
    perfil.pais=None
    perfil.save()