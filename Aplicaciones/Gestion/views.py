from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

# Renderizando el template de listado de Areas
def listadoAreas(request):
    return render(request,"Areas/listado.html")