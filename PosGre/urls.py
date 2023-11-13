from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_lista, name='cliente_list'),
    path('areas/', views.area_lista, name='area_list'),
    path('empleados/', views.empleado_lista, name='empleado_list'),
    path('ventas/', views.venta_lista, name='venta_list'),
]