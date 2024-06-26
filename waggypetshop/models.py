from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(primary_key=True, max_length=10)
    contraseña = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre