from django.db import models
from Aplicaciones.Gestion.models import Area, Responsable, Bloques, Variedades

class ConteoDiario(models.Model):
    fecha = models.DateField()
    dia = models.CharField(max_length=10)
    conteo_del_dia = models.IntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='conteos_diarios')
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, related_name='conteos_diarios')
    bloque = models.ForeignKey(Bloques, on_delete=models.CASCADE, related_name='conteos_diarios')
    variedad = models.ForeignKey(Variedades, on_delete=models.CASCADE, related_name='conteos_diarios')


    def __str__(self):
        return f'{self.fecha} - {self.dia}'
