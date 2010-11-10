from carreteras.models import *
from django.contrib import admin

class EstadoAdmin(admin.ModelAdmin):
    pass

class MunicipioAdmin(admin.ModelAdmin):
    pass

class LocalidadAdmin(admin.ModelAdmin):
    pass

class RutaAdmin(admin.ModelAdmin):
    pass

class CorredorAdmin(admin.ModelAdmin):
    pass

class CarreteraAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'ruta']}),
        ('IDs', {'fields': ['identificador_nacional']}),
    ]

class TramoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'carretera', 'corredor', 'origen', 'destino']}),
        (u'Caracter\u00edsticas',
            {'fields': ['tipo_red', 'km_inicio', 'km_fin', 'carriles', 'cuerpos']}),
        (u'Geo Ubicaci\u00f3n', {
            'fields': ['latitud_inicio', 'longitud_inicio', 'latitud_fin', 'longitud_fin'],
            'classes': ['collapse']
        }),
    ]

class SubtramoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'tramo']}),
        (u'Caracter\u00edsticas', {'fields': ['km_inicio', 'km_fin']}),
        (u'Geo Ubicaci\u00f3n', {
            'fields': ['latitud_inicio', 'longitud_inicio', 'latitud_fin', 'longitud_fin'],
            'classes': ['collapse']
        }),
    ]

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Corredor, CorredorAdmin)
admin.site.register(Carretera, CarreteraAdmin)
admin.site.register(Tramo, TramoAdmin)
admin.site.register(Subtramo, SubtramoAdmin)

