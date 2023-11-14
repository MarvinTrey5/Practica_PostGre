from django.db import models

# Create your models here.
# modelos para cada tabla
# 1
class Cliente(models.Model):
    id= models.AutoField(primary_key=True) # se añade una primary key de tipo booleana True
    Nombre = models.CharField(max_length=100) # tipo varchar.
    Apellido = models.CharField(max_length=100) # tipo varchar.
    Edad = models.PositiveIntegerField() # Tipo numérico.
    DUI = models.PositiveIntegerField()  # Tipo numérico.
# 2
class Area(models.Model):
    id = models.AutoField(primary_key=True) # Se añade una primary key de tipo booleana True.
    Nombre_del_area = models.CharField(max_length=200) # varchar.
    Descripcion = models.CharField(max_length=200)    # varchar.
# 3
class empleado(models.Model):
    id = models.AutoField(primary_key=True) # Se añade una primary key de tipo booleana True.
    Nombre = models.CharField(max_length=200) # varchar.
    Apellido = models.CharField(max_length=200) # varchar.
    Edad = models.PositiveIntegerField()  # Tipo numérico.
    AreaID = models.ForeignKey(Area, on_delete=models.CASCADE) # Se añade una llave fórane ya que tendra relación con la tabla Area del campo id.
# 4
class Venta(models.Model):
    id = models.AutoField(primary_key=True) # Se añade una primary key de tipo booleana True.
    Fecha_Venta = models.DateTimeField() # el formato será AAAA-MMMM-DDDD HHH:MMM:SS
    Monto = models.FloatField(max_length=100) # tipo flotante.
    Clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Se añade una llave fóranea que tendrá relación con la tabla cliente del campo id.
    EmpleadoID = models.ForeignKey(empleado,on_delete=models.CASCADE) # se añade una llave fóranea que tendrá relación con la tabla Empleado del campo id.
