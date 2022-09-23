from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    publicacion = models.IntegerField()

class Musica(models.Model):
    cancion = models.CharField(max_length=30)
    disco = models.CharField(max_length=30)
    grupo = models.CharField(max_length=30)
    año = models.IntegerField()

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    año = models.IntegerField()

