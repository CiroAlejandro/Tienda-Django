from django.contrib import admin
from .models import Cliente, Producto, Orden

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Orden)
# Register your models here.
