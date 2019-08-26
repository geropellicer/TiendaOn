from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=120)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, 
                                  on_delete=models.CASCADE,
                                  related_name="productos")
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    precio = models.FloatField()
    costo_envio = models.FloatField()
    cantidad = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
