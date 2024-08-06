from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Aplicaciones.Campo.views import conteo_diario_view,conteo_diario

urlpatterns = [
    #HOME
    path('',views.home, name='home'),
    path('Ingreso/diario.html', conteo_diario_view, name='conteo_diario_view'),
    path('Conteo/diario.html', conteo_diario, name='conteo_diario'),


    #LOGIN ADMINISTRADOR
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    #LOGIN AGENTE
    path('loginAgente/', views.loginAgente, name='loginAgente'),


    #LOGIN AGENTE
    path('loginLectura/', views.loginLectura, name='loginLectura'),


    path('inicio/', views.inicio, name='inicio'),
    path('inicioC/', views.inicioC, name='inicioC'),


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


    #BLOQUES
    path('Bloques/listado.html/', views.listadoBloques, name='listadoBloques'),
    path('Bloques/gestion.html/', views.gestionBloques, name='gestionBloques'),
    path('guardarBloque/', views.guardarBloque, name='guardarBloque'),
    path('eliminarBloque/<id>/', views.eliminarBloque, name='eliminarBloque'),
    path('editarBloque/<id>/', views.editarBloque, name='editarBloque'),
    path('procesarActualizacionBloque/', views.procesarActualizacionBloque, name='procesarActualizacionBloque'),

    #Variedades
    path('Variedades/listado.html/', views.listadoVariedades, name='listadoVariedades'),
    path('Variedades/gestion.html/', views.gestionVariedades, name='gestionVariedades'),
    path('guardarVariedad/', views.guardarVariedad, name='guardarVariedad'),
    path('procesarActualizacionVariedad/', views.procesarActualizacionVariedad, name='procesarActualizacionVariedad'),
    path('eliminarVariedad/<id>/', views.eliminarVariedad, name='eliminarVariedad'),
    path('editarVariedad/<id>/', views.editarVariedad, name='editarVariedad'),
    

]
