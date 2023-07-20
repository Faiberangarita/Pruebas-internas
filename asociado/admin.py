from django.contrib import admin
from asociado.models import usuario, asociado, servicio, producto, oferta, categoria, tipoasoc, Noticia

# Register your models here.
admin.site.register(usuario)
admin.site.register(asociado)
admin.site.register(servicio)
admin.site.register(producto)
admin.site.register(categoria)
admin.site.register(tipoasoc)
admin.site.register(Noticia)
admin.site.register(oferta)