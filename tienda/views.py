from django.shortcuts import render , get_object_or_404
from .models import Producto, Cliente, Pedido

'''Vista para la página de inicio de la tienda.

 Muestra una lista de productos disponibles y permite a los clientes navegar por ellos.'''
def home(request):
    return render(request, "tienda/home.html" , {})

'''
Vista para el listado de productos.

'''

def listado_productos(request):
    # Aquí iría la lógica para obtener los productos de la base de datos   
    productos = Producto.objects.all().order_by("nombre")  # Ejemplo de ordenamiento por nombre
    return render(request, "tienda/lista_productos.html", {"productos": productos})

'''
Vista de detalle de un producto 
'''

def detalle_producto(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})