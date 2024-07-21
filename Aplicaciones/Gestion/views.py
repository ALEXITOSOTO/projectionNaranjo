from django.http import JsonResponse
from django.shortcuts import render
from .models import Area

# Create your views here.
def home(request):
    return render(request,"home.html")

def gestionAreas(request):
    return render(request,'Areas/gestion.html')

# Renderizando el template de listado de Areas
def listadoAreas(request):
    areasBdd = Area.objects.all()
    return render(request,"Areas/listado.html",{"areas":areasBdd})

def guardarArea(request):
    cod=request.POST["codigo"]
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    nuevaArea=Area.objects.create(codigo=cod,nombre=nom,descripcion=des)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Área registrada exitosamente.'
    })
