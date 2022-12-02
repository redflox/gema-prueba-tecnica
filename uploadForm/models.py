from django.db import models

# Create your models here.

class Archivo(models.Model):
    name = models.CharField(max_length=50)


class Estado(models.Model):
    name = models.CharField(max_length=50)

class Revisor(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

class Usuario(models.Model):
    email = models.EmailField(max_length=150)
    name = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    revisor = models.ForeignKey(Revisor, default="", on_delete=models.CASCADE)