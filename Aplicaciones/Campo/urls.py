from django.urls import path
from . import views

urlpatterns = [
    path('Conteo/diario.html',views.registro_diario, name='ingresoDiario'),
    path('Ingreso/diario.html', views.mostrar_conteos, name='mostrar_conteos')
]