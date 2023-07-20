from codezilla.views import inicio
"""codezilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from codezilla.views import tienda,carrito,ofertas,somos,cuenta,contacto,servicio_f,agregar_producto,eliminar_producto,restar_producto,limpiar_carro,agregart_producto, VRegistro, cerrar_sesion, logear
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('servicios/', servicio_f),
    path('inicio/', inicio),
    path('tienda/', tienda, name="tienda"),
    path('carrito/', carrito, name="carrito"),
    path('ofertas/', ofertas),
    path('somos/', somos),
    path('cuenta/', cuenta),
    path('contacto/', contacto),
    path("agregar/<int:producto_id>",agregar_producto, name="agregar" ),
    path("agregart/<int:producto_id>",agregart_producto, name="agregart" ),
    path("eliminar/<int:producto_id>",eliminar_producto, name="eliminar" ),
    path("restar/<int:producto_id>",restar_producto, name="restar" ),
    path("limpiar/",limpiar_carro, name="limpiar" ),
    
    path('Autenticacion/',VRegistro.as_view(), name="Autenticacion"),
    path('Autenticacion/cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('login/',logear, name="logear"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)