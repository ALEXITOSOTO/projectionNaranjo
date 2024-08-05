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

class Responsable(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20, unique=True, default='0000000000')
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.area.codigo}'

class Bloques(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=250, unique=True)
    nombre=models.CharField(max_length=250)
    descripcion=models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        fila='{0} - {1} - {2}'
        return fila.format(self.id,self.codigo,self.descripcion)
    
class Variedades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, default='No ingresado')
    caracteristicas = models.TextField(default='Descripción no proporcionada')

    def __str__(self):
        return self.nombre
