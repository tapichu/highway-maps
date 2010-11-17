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
    estado = models.ForeignKey(Estado, related_name='municipios')

    def __unicode__(self):
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, related_name='localidades')

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
    ruta = models.ForeignKey(Ruta, related_name='carreteras')
    fecha_modificacion = models.DateTimeField(u'Fecha \u00faltima modificaci\u00f3n', auto_now=True)

    def __unicode__(self):
        return self.nombre

class Tramo(LineGeoLocation):
    carretera = models.ForeignKey(Carretera, related_name='tramos')
    nombre = models.CharField(max_length=100)
    estados = models.ManyToManyField(Estado, related_name='tramos')
    municipios = models.ManyToManyField(Municipio, related_name='tramos')
    localidad = models.ForeignKey(Localidad, related_name='tramos')
    corredor = models.ForeignKey(Corredor, blank=True, null=True, related_name='tramos')
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
        return (float(self.km_fin * 1000) - float(self.km_inicio * 1000)) / 1000;

class Subtramo(LineGeoLocation):
    tramo = models.ForeignKey(Tramo, related_name='subtramos')
    nombre = models.CharField(max_length=100)
    km_inicio = models.DecimalField(max_digits=10, decimal_places=4)
    km_fin = models.DecimalField(max_digits=10, decimal_places=4)
    fecha_modificacion = models.DateTimeField(u'Fecha \u00faltima modificaci\u00f3n', auto_now=True)

    def __unicode__(self):
        return self.nombre

    def longitud(self):
        return (float(self.km_fin * 1000) - float(self.km_inicio * 1000)) / 1000;

