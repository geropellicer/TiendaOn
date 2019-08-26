from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Producto, Proveedor

# Create your views here.
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detalles.html"

class ProductoListaView(ListView):
    model = Producto
    template_name = "productos/producto_lista.html"    