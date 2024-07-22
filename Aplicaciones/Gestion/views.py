from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
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

def eliminarArea(request, id):
    areaEliminar = Area.objects.get(id=id)
    areaEliminar.delete()
    messages.success(request, 'Area eliminada exitosamente.')
    return redirect('gestionAreas')


def editarArea(request, id):
    areaEditar = Area.objects.get(id=id)
    return render(request, 'Areas/editar.html', {'areaEditar': areaEditar})

def procesarActualizacionArea(request):
    id = request.POST['id']
    cod = request.POST['codigo']
    nom = request.POST['nombre']
    des = request.POST['descripcion']
    AreaConsultado = Area.objects.get(id=id)
    AreaConsultado.codigo = cod
    AreaConsultado.nombre = nom
    AreaConsultado.descripcion = des
    AreaConsultado.save()
    messages.success(request, 'Area actualizada exitosamente.')
    return redirect('gestionAreas')

