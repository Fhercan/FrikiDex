from django.shortcuts import render,redirect
# Create your views here.
def index(request):
    return render(request,'perfiles.listado.html')

def editarPerfil(request):
    return render(request,'perfil.editar.html')