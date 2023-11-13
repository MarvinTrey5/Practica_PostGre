from django.db import models

# Create your models here.
class Cliente(models.Model):
    id= models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Edad = models.PositiveIntegerField()
    DUI = models.PositiveIntegerField()

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_del_area = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)    

class empleado(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Edad = models.PositiveIntegerField()
    AreaID = models.ForeignKey(Area, on_delete=models.CASCADE)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha_Venta = models.DateTimeField()
    Monto = models.FloatField(max_length=100)
    Clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    EmpleadoID = models.ForeignKey(empleado,on_delete=models.CASCADE)
