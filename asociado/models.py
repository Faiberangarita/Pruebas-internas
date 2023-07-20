from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    carrera=models.CharField(max_length=25)
    codigo=models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    fecha_nacimiento=models.DateField()
    imagen=models.ImageField(upload_to="usuario", null=True, blank=True)

    def __str__(self):
        return self.nombre 

class tipoasoc(models.Model):
    nombre=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class asociado(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    carrera=models.CharField(max_length=25)
    codigo=models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    tipo=models.ForeignKey(tipoasoc, on_delete=models.CASCADE)
    informacion=models.CharField(max_length=350)
    fecha_nacimiento=models.DateField()
    imagen=models.ImageField(upload_to="asociado", null=True, blank=True)

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
    
class categoria(models.Model):
    nombre=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    precio=models.FloatField()
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE)
    Disponibilidad=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to="producto")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class oferta(models.Model):
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=350)
    precio=models.FloatField()
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE)
    Disponibilidad=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to="oferta")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=850)
    imagen=models.ImageField(upload_to="noticia", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo