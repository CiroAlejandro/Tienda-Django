from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=32)
    cedula = models.CharField(max_length=16)
    def __str__(self):
        return str(self.nombre) + str(self.cedula)

class Producto(models.Model):
    nombre = models.CharField(max_length=32)
    precio = models.FloatField()
    referencia = models.CharField(max_length=16)
    def __str__(self):
        return str(self.referencia)


def generar_codigo():
    v = Orden.objects.count()
    return v + 1


class Orden(models.Model):
    codigo = models.IntegerField(generar_codigo)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    producto_id = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return str(self.codigo)



# Create your models here.
