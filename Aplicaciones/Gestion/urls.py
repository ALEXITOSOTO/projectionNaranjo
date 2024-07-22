# Configurando redireccionamiento
from django.urls import path
from . import views #Importando todas las vistas de views.py

urlpatterns = [
    path('',views.home, name='home'),
    path('Areas/listado.html/', views.listadoAreas, name='listadoAreas'),
    path('Areas/gestion.html/', views.gestionAreas, name='gestionAreas'),
    path('guardarArea/', views.guardarArea, name='guardarArea'),
    path('procesarActualizacionArea/', views.procesarActualizacionArea, name='procesarActualizacionArea'),
    path('eliminarArea/<id>/', views.eliminarArea, name='eliminarArea'),
    path('editarArea/<id>/', views.editarArea, name='editarArea'),
]