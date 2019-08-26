from django.urls import path
from .views import ProductoDetailView, ProductoListaView

urlpatterns = [
    path('', ProductoListaView.as_view(), name="lista-productos"),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name="detalles-producto"),
]