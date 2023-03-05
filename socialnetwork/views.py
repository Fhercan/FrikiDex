from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from logros.models import Logro
from .models import Megusta
#from .forms import CapturaForm,LogroForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        logros = Logro.objects.filter(publicar=True).exclude(user=request.user).order_by('-created_date')
        return render(request,'publicaciones.html',{'logros':logros})
    else:
        return render(request,'home.html')
    
@login_required(login_url='account_login')
def likePublicacion(request):
    if request.method=="POST":
        logro=Logro.objects.get(id=request.POST['id'])
        #Verificar que el usuario logueado no sea el creador del Logro
        if logro.user.id != request.user.id:
            #Verificar si ya le habia dado like
            megustas=Megusta.objects.filter(user=request.user,logro=logro)
            if megustas.count() == 0:
                megusta=Megusta()
                megusta.user=request.user
                megusta.logro=logro
            else:
                megusta=megustas[0]
                megusta.estatus_megusta = not megusta.estatus_megusta
            megusta.save()
            if megusta.estatus_megusta:
                #Registrar el like
                logro.megustas+=1
            else:
                #Quitar el like
                logro.megustas-=1
            logro.save()
        return JsonResponse({'resultado':True,'like':logro.megustas})
    else:
        return JsonResponse({'resultado':False,'mensaje':'error'})