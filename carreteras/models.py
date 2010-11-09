from django.db import models
from carreteras.commons import ESTADOS_CHOICES

class Estado(models.Model):
    nombre = models.CharField(max_length=100, unique=True, choices=ESTADOS_CHOICES)

    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

class Ruta(models.Model):
    numero = models.IntegerField()

    def __unicode__(self):
        return "MEX-" + self.numero

class Carretera(models.Model):
    identificadorNacional = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    ruta = models.ForeignKey(Ruta)

    def __unicode__(self):
        return self.identificadorNacional + ": " + self.nombre

