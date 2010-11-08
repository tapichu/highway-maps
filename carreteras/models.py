from django.db import models

class Carretera(models.Model):
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    de_km = models.DecimalField(max_digits=10, decimal_places=4)
    a_km = models.DecimalField(max_digits=10, decimal_places=4)
    comentarios = models.CharField(max_length=1000)
    version = models.IntegerField()

