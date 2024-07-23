from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    #AREAS
    path('Areas/listado.html/', views.listadoAreas, name='listadoAreas'),
    path('Areas/gestion.html/', views.gestionAreas, name='gestionAreas'),
    path('guardarArea/', views.guardarArea, name='guardarArea'),
    path('procesarActualizacionArea/', views.procesarActualizacionArea, name='procesarActualizacionArea'),
    path('eliminarArea/<id>/', views.eliminarArea, name='eliminarArea'),
    path('editarArea/<id>/', views.editarArea, name='editarArea'),



    # RESPONSABLES
    path('Responsables/listado.html/', views.listadoResponsables, name='listadoResponsables'),
    path('Responsables/gestion.html/', views.gestionResponsables, name='gestionResponsables'),
    path('guardarResponsable/', views.guardarResponsable, name='guardarResponsable'),
    path('eliminarResponsable/<id>/', views.eliminarResponsable, name='eliminarResponsable'),
    path('editarResponsable/<id>/', views.editarResponsable, name='editarResponsable'),
    path('procesarActualizacionResponsable/', views.procesarActualizacionResponsable, name='procesarActualizacionResponsable'),
]
