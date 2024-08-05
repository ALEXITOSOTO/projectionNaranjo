from django.contrib import admin
from .models import ConteoDiario

@admin.register(ConteoDiario)
class ConteoDiarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'dia', 'conteo_del_dia', 'area', 'responsable', 'bloque', 'variedad')