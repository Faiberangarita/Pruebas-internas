from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail   import send_mail
from django.conf import settings
from asociado.models import oferta, producto, servicio, asociado, usuario

def inicio(request):
    return render(request,"inicio.html")

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
    return render(request,"cuenta.html")

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