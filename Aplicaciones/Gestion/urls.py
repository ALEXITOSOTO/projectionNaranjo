# Configurando redireccionamiento
from django.urls import path
from . import views #Importando todas las vistas de views.py

urlpatterns = [
    path('',views.home),
    path('listadoAreas/', views.listadoAreas)
]