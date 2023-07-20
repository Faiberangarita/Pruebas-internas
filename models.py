from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    carrera=models.CharField(max_length=25)
    codigo=models.CharField(max_length=10, default='0000000')
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.nombre 
class categoria(models.Model):
    nombre=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre 
    
class asociado(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    carrera=models.CharField(max_length=25)
    codigo=models.CharField(max_length=10, default='0000000')
    fecha_nacimiento=models.DateField()
    tipo_socio=models.IntegerField()

    def __str__(self):
        return self.nombre 

class servicio(models.Model):
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    precio=models.CharField(max_length=25)
    imagen=models.ImageField(upload_to="servicio")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo 

class producto(models.Model):
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    precio=models.CharField(max_length=15)
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE, default='100')
    seccion=models.CharField(max_length=20)
    Disponibilidad=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to="producto")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class oferta(models.Model):
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    precio=models.CharField(max_length=15)
    seccion=models.CharField(max_length=20)
    Disponibilidad=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to="producto")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Noticia(models.Model):
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    imagen=models.ImageField(upload_to="noticia", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo