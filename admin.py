from django.contrib import admin
from asociado.models import usuario, asociado, servicio, producto, oferta

# Register your models here.
class cusuario(admin.ModelAdmin):
    list_display=("nombre","apellido","carrera","fecha_nacimiento")
    search_fields=("nombre","apellido","carrera")
    list_filter=("carrera",)
    date_hierarchy=("fecha_nacimiento")

class cservicio(admin.ModelAdmin):
    list_display=("titulo","precio","updated")
    search_fields=("titulo","precio","updated")
    date_hierarchy=("updated")

class cproducto(admin.ModelAdmin):
    list_display=("titulo","precio","updated","seccion")
    search_fields=("titulo","precio","updated")
    date_hierarchy=("updated")

admin.site.register(usuario,cusuario)
admin.site.register(asociado,cusuario)
admin.site.register(servicio,cservicio)
admin.site.register(producto,cproducto)
admin.site.register(oferta,cproducto)