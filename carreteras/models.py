from django.db import models
from carreteras.commons import ESTADOS_CHOICES, TIPO_RED_CHOICES

class LineGeoLocation(models.Model):
    latitud_inicio = models.DecimalField(max_digits=7, decimal_places=4, default=0.0)
    latitud_fin = models.DecimalField(max_digits=7, decimal_places=4, default=0.0)
    longitud_inicio = models.DecimalField(max_digits=7, decimal_places=4, default=0.0)
    longitud_fin = models.DecimalField(max_digits=7, decimal_places=4, default=0.0)

    class Meta:
        abstract = True

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

    class Meta:
        verbose_name_plural = 'Localidades'

class Ruta(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return 'MEX-' + str(self.numero)

class Corredor(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return 'C-' + str(self.numero)

    class Meta:
        verbose_name_plural = 'Corredores'

class Carretera(models.Model):
    identificador_nacional = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    ruta = models.ForeignKey(Ruta)
    fecha_modificacion = models.DateTimeField(u'Fecha \u00faltima modificaci\u00f3n', auto_now=True)

    def __unicode__(self):
        return self.identificadorNacional + ": " + self.nombre

class Tramo(LineGeoLocation):
    carretera = models.ForeignKey(Carretera)
    nombre = models.CharField(max_length=100)
    estados = models.ManyToManyField(Estado)
    municipios = models.ManyToManyField(Municipio)
    localidad = models.ForeignKey(Localidad)
    corredor = models.ForeignKey(Corredor, blank=True)
    tipo_red = models.CharField(max_length=1, choices=TIPO_RED_CHOICES)
    km_inicio = models.DecimalField(max_digits=10, decimal_places=4)
    km_fin = models.DecimalField(max_digits=10, decimal_places=4)
    carriles = models.IntegerField()
    cuerpos = models.IntegerField()
    # TODO: origen y destino pueden ser municipio, localidad o km
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_modificacion = models.DateTimeField(u'Fecha \u00faltima modificaci\u00f3n', auto_now=True)

    def __unicode__(self):
        return self.nombre

    def longitud(self):
        return self.km_fin - self.km_inicio;

class Subtramo(LineGeoLocation):
    tramo = models.ForeignKey(Tramo)
    nombre = models.CharField(max_length=100)
    km_inicio = models.DecimalField(max_digits=10, decimal_places=4)
    km_fin = models.DecimalField(max_digits=10, decimal_places=4)
    fecha_modificacion = models.DateTimeField(u'Fecha \u00faltima modificaci\u00f3n', auto_now=True)

    def __unicode__(self):
        return self.nombre

    def longitud(self):
        return self.km_fin - self.km_inicio;

