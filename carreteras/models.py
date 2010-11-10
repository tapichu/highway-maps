from django.db import models
from carreteras.commons import ESTADOS_CHOICES, TIPO_RED_CHOICES

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

class Corredor(models.Model):
    numero = models.IntegerField()

    def __unicode__(self):
        return "C-" + self.numero

class Carretera(models.Model):
    identificador_nacional = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    ruta = models.ForeignKey(Ruta)
    fecha_modificacion = models.DateField(u'Fecha \u00faltima modificaci\u00f3n')

    def __unicode__(self):
        return self.identificadorNacional + ": " + self.nombre

class Tramo(models.Model):
    nombre = models.CharField(max_length=100)
    carretera = models.ForeignKey(Carretera)
    corredor = models.ForeignKey(Corredor)
    tipo_red = models.CharField(max_length=1, choices=TIPO_RED_CHOICES)
    longitud = models.DecimalField(max_digits=10, decimal_places=4)
    km_inicio = models.DecimalField(max_digits=10, decimal_places=4)
    km_fin = models.DecimalField(max_digits=10, decimal_places=4)
    carriles = models.IntegerField()
    cuerpos = models.IntegerField()
    # TODO: origen y destino pueden ser municipio, localidad o km
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

