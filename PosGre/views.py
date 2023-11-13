from django.shortcuts import render
from . models import Cliente, Area, empleado, Venta
# Create your views here.

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_lista.html', {'clientes': clientes})

def area_lista(request):
    areas = Area.objects.all()
    return render(request, 'area_lista.html', {'areas': areas})

def empleado_lista(request):
    empleados = empleado.objects.all()
    return render(request, 'empleados_lista.html', {'empleados': empleados})

def venta_lista(request):
    ventas = Venta.objects.all()
    return render(request, 'venta_lista.html', {'ventas': ventas})