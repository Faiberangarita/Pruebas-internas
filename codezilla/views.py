from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail   import send_mail
from django.conf import settings
from asociado.models import oferta, producto, servicio, asociado, usuario, Noticia

from asociado.carro import Carro


from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def inicio(request):
    carro=Carro(request)
    noticias=Noticia.objects.all()
    return render(request,"inicio.html",{"noticias":noticias})

def servicio_f(request):
    servicios=servicio.objects.all()
    
    return render(request,"servicios.html",{"servicios":servicios})

def tienda(request):
    productos=producto.objects.all()
    
    return render(request,"tienda.html",{"productos": productos})

def carrito(request):
    return render(request,"carrito.html")

def ofertas(request):
    ofertas=oferta.objects.all()
    
    return render(request,"ofertas.html",{"ofertas": ofertas})

def somos(request):
    return render(request,"somos.html")

def cuenta(request):
    return render(request,"menu.html")

def contacto(request):
    if request.method=="POST":
        Enombre=request.POST["nombre"]
        Easunto=request.POST["asunto"]
        Email=request.POST["correo"]
        Emensaje=request.POST["mensaje"] + " " + Enombre + " " + Email
        recipiente=["faiberangaritamendoza@gmail.com"]
        email_from=settings.EMAIL_HOST_USER
        send_mail(Easunto,Emensaje,email_from,recipiente)

        return render(request,"gracias.html")

    return render(request,"contacto.html")


def agregar_producto(request, producto_id):

    carro=Carro(request)

    Producto=producto.objects.get(id=producto_id)

    carro.agregar(producto=Producto)

    return redirect("carrito")

def agregart_producto(request, producto_id):

    carro=Carro(request)

    Producto=producto.objects.get(id=producto_id)

    carro.agregar(producto=Producto)

    return redirect("tienda")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    Producto=producto.objects.get(id=producto_id)

    carro.eliminar(producto=Producto)

    return redirect("carrito")


def restar_producto(request, producto_id):

    carro=Carro(request)

    Producto=producto.objects.get(id=producto_id)

    carro.restar_producto(producto=Producto)

    return redirect("carrito")


def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("carrito")



class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('inicio')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)

    return redirect('inicio')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

