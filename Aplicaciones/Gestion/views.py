from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Area, Responsable, Bloques, Variedades
from django.contrib.auth.decorators import login_required #Pra el login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Q
from datetime import date, timedelta
from Aplicaciones.Campo.models import ConteoDiario
from django.db.models import Sum, Case, When, IntegerField
# Create your views here.

def home(request):
    return render(request, "home.html")



#LOGIN ADMINISTRADOR
@csrf_exempt  
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def custom_logout(request):
    logout(request)
    return redirect('login')


#LOGIN AGENTE DE CAMPO
def loginAgente(request):
    return render(request, "registration/loginAgente.html")

#LOGIN USUARIO DE LECCTURA
def loginLectura(request):
    return render(request, "registration/loginLectura.html")


#AREAS
@login_required
def inicio(request):
    return render(request,'inicio.html')
                
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



#RESPONSABLE
def listadoResponsables(request):
    responsablesBdd = Responsable.objects.all()
    return render(request, "Responsables/listado.html", {"responsables": responsablesBdd})

def gestionResponsables(request):
    areas = Area.objects.all()
    return render(request, 'Responsables/gestion.html', {'areas': areas})

def guardarResponsable(request):
    nom = request.POST["nombre"]
    ape = request.POST["apellido"]
    email = request.POST["email"]
    tel = request.POST["telefono"]
    ced = request.POST["cedula"]
    area_id = request.POST["area"]
    estado = request.POST["estado"]
    area = Area.objects.get(id=area_id)
    
    nuevoResponsable = Responsable.objects.create(
        nombre=nom,
        apellido=ape,
        email=email,
        telefono=tel,
        cedula=ced,
        area=area,
        estado=estado
    )
    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Responsable registrado exitosamente.'
    })

def eliminarResponsable(request, id):
    responsableEliminar = Responsable.objects.get(id=id)
    responsableEliminar.delete()
    messages.success(request, 'Responsable eliminado exitosamente.')
    return redirect('gestionResponsables')

def editarResponsable(request, id):
    responsableEditar = Responsable.objects.get(id=id)
    areas = Area.objects.all()
    return render(request, 'Responsables/editar.html', {'responsableEditar': responsableEditar, 'areas': areas})

def procesarActualizacionResponsable(request):
    id = request.POST['id']
    nom = request.POST['nombre']
    ape = request.POST['apellido']
    email = request.POST['email']
    tel = request.POST['telefono']
    ced = request.POST['cedula']
    area_id = request.POST["area"]
    estado = request.POST["estado"]
    area = Area.objects.get(id=area_id)
    
    ResponsableConsultado = Responsable.objects.get(id=id)
    ResponsableConsultado.nombre = nom
    ResponsableConsultado.apellido = ape
    ResponsableConsultado.email = email
    ResponsableConsultado.telefono = tel
    ResponsableConsultado.cedula = ced
    ResponsableConsultado.area = area
    ResponsableConsultado.estado = estado
    ResponsableConsultado.save()
    
    messages.success(request, 'Responsable actualizado exitosamente.')
    return redirect('gestionResponsables')


#BLOQUE
def listadoBloques(request):
    bloques = Bloques.objects.all()
    return render(request, "Bloques/listado.html", {"bloques": bloques})

def gestionBloques(request):
    areas = Area.objects.all()
    return render(request, 'Bloques/gestion.html', {'areas': areas})

def guardarBloque(request):
    codigo = request.POST["codigo"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    area_id = request.POST["area"]
    area = Area.objects.get(id=area_id)
    
    nuevoBloque = Bloques.objects.create(
        codigo=codigo,
        nombre=nombre,
        descripcion=descripcion,
        area=area
    )
    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Bloque registrado exitosamente.'
    })

def eliminarBloque(request, id):
    bloqueEliminar = Bloques.objects.get(id=id)
    bloqueEliminar.delete()
    messages.success(request, 'Bloque eliminado exitosamente.')
    return redirect('gestionBloques')

def editarBloque(request, id):
    bloqueEditar = Bloques.objects.get(id=id)
    areas = Area.objects.all()
    return render(request, 'Bloques/editar.html', {'bloqueEditar': bloqueEditar, 'areas': areas})

def procesarActualizacionBloque(request):
    id = request.POST['id']
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    area_id = request.POST["area"]
    area = Area.objects.get(id=area_id)
    
    bloqueConsultado = Bloques.objects.get(id=id)
    bloqueConsultado.codigo = codigo
    bloqueConsultado.nombre = nombre
    bloqueConsultado.descripcion = descripcion
    bloqueConsultado.area = area
    bloqueConsultado.save()
    
    messages.success(request, 'Bloque actualizado exitosamente.')
    return redirect('gestionBloques')



# Listar Variedades
def listadoVariedades(request):
    variedades = Variedades.objects.all()
    return render(request, "Variedades/listado.html", {"variedades": variedades})

# Gestión de Variedades
def gestionVariedades(request):
    variedades = Variedades.objects.all()
    return render(request, 'Variedades/gestion.html', {'areas': variedades})

# Guardar Variedad
def guardarVariedad(request):
    nombre = request.POST["nombre"]
    ciclo_fenologico = request.POST["ciclo_fenologico"]
    dias_ciclo = request.POST["dias_ciclo"]
    caracteristicas = request.POST["caracteristicas"]
    estado = request.POST["estado"]

    nuevaVariedad = Variedades.objects.create(
            nombre=nombre,
            ciclo_fenologico=ciclo_fenologico,
            dias_ciclo=dias_ciclo,
            caracteristicas=caracteristicas,
            estado=estado
        )
    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Variedad registrada exitosamente.'
    })

# Eliminar Variedad
def eliminarVariedad(request, id):
    variedadEliminar = Variedades.objects.get(id=id)
    variedadEliminar.delete()
    messages.success(request, 'Variedad eliminada exitosamente.')
    return redirect('gestionVariedades')

# Editar Variedad
def editarVariedad(request, id):
    variedadEditar = Variedades.objects.get(id=id)
    return render(request, 'Variedades/editar.html', {'variedadEditar': variedadEditar})

# Procesar Actualización de Variedad
def procesarActualizacionVariedad(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    caracteristicas = request.POST['caracteristicas']
    ciclo_fenologico = request.POST['ciclo_fenologico']
    dias_ciclo = request.POST['dias_ciclo']
    estado = request.POST['estado']
    
    variedadConsultada = Variedades.objects.get(id=id)
    variedadConsultada.nombre = nombre
    variedadConsultada.caracteristicas = caracteristicas
    variedadConsultada.ciclo_fenologico = ciclo_fenologico
    variedadConsultada.dias_ciclo = dias_ciclo
    variedadConsultada.estado = estado
    variedadConsultada.save()
    
    messages.success(request, 'Variedad actualizada exitosamente.')
    return redirect('gestionVariedades')



def diario(request):
    return render(request, "Conteos/diario.html")




