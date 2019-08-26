from django.urls import path
# from .views import ProductoDetailView, ProductoListaView
from .views import lista_productos, detalles_producto, lista_proveedores, detalles_proveedor

# urlpatterns = [
#     path('', ProductoListaView.as_view(), name="lista-productos"),
#     path('productos/<int:pk>/', ProductoDetailView.as_view(), name="detalles-producto"),
# ]

urlpatterns = [
    path('productos/', lista_productos, name="lista-productos"),
    path('productos/<int:pk>', detalles_producto, name="detalles-producto"),
    path('proveedores/', lista_proveedores, name="lista-proveedores"),
    path('proveedores/<int:pk>', detalles_proveedor, name="detalles-proveedor"),
]