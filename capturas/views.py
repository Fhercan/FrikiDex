from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Captura
from logros.models import Logro
from .forms import CapturaForm

# Create your views here.
@login_required(login_url='account_login')
def indexCapturas(request):
    capturas = Captura.objects.filter(user=request.user).order_by('numero_pokemon')
    return render(request,'capturas.listado.html',{'capturas':capturas})
   

@login_required(login_url='account_login')
def editarCaptura(request, id):
    if request.method=="GET":
        #Editar o nuevo
        if id>0:
            #Es logro existente se busca el logro y se genera el formulario en base al registro
            captura=Captura.objects.get(id=id)
            form=CapturaForm(instance=captura)
        else:
            #Es nuevo logro se genera el formulario en blanco
            form=CapturaForm()
    else:
        print(request.POST)
        if id>0:
            captura=Captura.objects.get(id=id)
            form=CapturaForm(request.POST, instance=captura)
            if form.is_valid():
                form.save()
                return redirect('indexcapturas')
        else:
            form=CapturaForm(request.POST)
            if form.is_valid():
                captura=form.save(commit=False)
                captura.user=request.user
                captura.save()
                #Registrar como el logro
                logro=Logro()
                logro.titulo='Captura'
                logro.user=request.user
                logro.comentarios='Ha capturado al  '+captura.nombre_pokemon
                logro.captura=captura
                logro.save()
                return redirect('indexcapturas')
    return render(request,'captura.editar.html',{'id':id,'form':form})
