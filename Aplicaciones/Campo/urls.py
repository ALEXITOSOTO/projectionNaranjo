from django.urls import path
from . import views

urlpatterns = [
    path('Conteo/diario.html', views.conteo_diario, name='conteoDiario'),
    path('Ingreso/diario.html', views.conteo_diario_view, name='ingresoDiario'),
    path('obtener_camas_bloque/', views.obtener_camas_bloque, name='obtener_camas_bloque'),
    path('reporte/', views.generar_reporte, name='generar_reporte'),  # Nueva ruta para el reporte
]
