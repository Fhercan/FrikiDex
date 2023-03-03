from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Logro
from .forms import LogroForm
from capturas.models import Captura

# Create your views here.
@login_required(login_url='account_login')
def indexLogros(request):
    logros = Logro.objects.filter(user=request.user).order_by('-created_date')
    return render(request,'logros.listado.html',{'logros':logros})

@login_required(login_url='account_login')
def editarLogro(request,id):
    if request.method=="GET":
        #Editar o nuevo
        if id>0:
            #Es logro existente se busca el logro y se genera el formulario en base al registro
            logro=Logro.objects.get(id=id)
            form=LogroForm(instance=logro)
        else:
            #Es nuevo logro se genera el formulario en blanco
            form=LogroForm()
    else:
        #markdownify
        #Es logro existente
        if id>0:
            logro=Logro.objects.get(id=id)
            form=LogroForm(request.POST, request.FILES, instance=logro)
            if form.is_valid():
                form.save()
                return redirect('indexlogros')
        else:
            form=LogroForm(request.POST, request.FILES)
            if form.is_valid():
                logro=form.save(commit=False)
                logro.user=request.user
                #captura=Captura.objects.get(id=1)
                #logro.captura=captura
                logro.save()
                return redirect('indexlogros')
    return render(request,'logro.editar.html',{'form':form})

@login_required(login_url='account_login')
def publicarLogro(request):
    if request.method=="POST":
        logro=Logro.objects.get(id=request.POST['id'])
        logro.publicar =True
        logro.save()
        return JsonResponse({'resultado':True,'like':logro.megustas})
    else:
        return JsonResponse({'resultado':False,'mensaje':'error'})
    
@login_required(login_url='account_login')
def nopublicarLogro(request):
    if request.method=="POST":
        logro=Logro.objects.get(id=request.POST['id'])
        logro.publicar = False
        logro.save()
        return JsonResponse({'resultado':True,'like':logro.megustas})
    else:
        return JsonResponse({'resultado':False,'mensaje':'error'})
    
@login_required(login_url='account_login')
def borrarLogro(request, id):
    if request.method=="POST":
        #Registrar el like
        logro=Logro.objects.get(id=id)
        logro.delete()
        return redirect('indexlogros')
    else:
        return JsonResponse({'resultado':False,'mensaje':'error'})