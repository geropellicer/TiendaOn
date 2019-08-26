# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# from .models import Producto, Proveedor

# # Create your views here.
# class ProductoDetailView(DetailView):
#     model = Producto
#     template_name = "productos/producto_detalles.html"

# class ProductoListaView(ListView):
#     model = Producto
#     template_name = "productos/producto_lista.html"    

from django.http import JsonResponse
from .models import Producto, Proveedor

def lista_productos(request):
    productos = Producto.objects.all()
    data = {"Productos": list(productos.values("pk", "nombre"))}
    respuesta = JsonResponse(data)
    return respuesta

def detalles_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        data = {"producto":{
                "nombre": producto.nombre,
                "proveedor": producto.proveedor.nombre,
                "descripcion": producto.descripcion,
                "foto": producto.foto.url,
                "precio": producto.precio,
                "costo de envio": producto.costo_envio,
                "cantidad": producto.cantidad,
            }
        }
        respuesta = JsonResponse(data)
    except Producto.DoesNotExist:
        respuesta = JsonResponse({
            "error": {
                "codigo": 404,
                "mensaje": "Producto inexistente",
            }}, status=404)
    return respuesta

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        "proveedores":list(proveedores.values())
    }
    respuesta = JsonResponse(data)
    return respuesta

def detalles_proveedor(request, pk):
    try:
        proveedor = Proveedor.objects.get(pk=pk)
        data = {
            "detalles del proveedor":{
                "Nombre del proveedor": proveedor.nombre,
                "Ubicacion": proveedor.ubicacion,
                "Activo": proveedor.activo,
            }
        }
        return JsonResponse(data)
    except Proveedor.DoesNotExist:
        data = {
            "Error":{
                "Codigo": 404,
                "Mensaje": "Producto no encontrado"
            }
        }
        respuesta = JsonResponse(data, status=404)
        return respuesta