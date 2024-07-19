from django.db import models

# Create your models here.
class Area(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=250, unique=True)
    nombre=models.CharField(max_length=250)
    descripcion=models.TextField()

    def __str__(self):
        fila='{0} - {1} - {2}'
        return fila.format(self.id,self.codigo,self.descripcion)
