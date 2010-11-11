from carreteras.models import *
from django.contrib import admin

class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    list_filter = ['estado']
    search_fields = ['nombre']

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'municipio')
    search_fields = ['nombre']

class RutaAdmin(admin.ModelAdmin):
    search_fields = ['numero']

class CorredorAdmin(admin.ModelAdmin):
    search_fields = ['numero']

class CarreteraAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'ruta']}),
        ('IDs', {'fields': ['identificador_nacional']}),
    ]
    list_display = ('nombre', 'ruta', 'identificador_nacional')
    list_filter = ['ruta']
    search_fields = ['nombre', 'identificador_nacional']

class TramoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': ['nombre', 'carretera', 'corredor', 'origen', 'destino']}),
        (u'Caracter\u00edsticas',
            {'fields': ['tipo_red', 'km_inicio', 'km_fin', 'carriles', 'cuerpos']}),
        (u'Ubicaci\u00f3n', {'fields': ['estados', 'municipios', 'localidad']}),
        (u'Geo Ubicaci\u00f3n', {
            'fields': ['latitud_inicio', 'longitud_inicio', 'latitud_fin', 'longitud_fin'],
            'classes': ['collapse']
        }),
    ]
    list_display = ('nombre', 'carretera', 'corredor', 'origen', 'destino')
    list_filter = ['carretera', 'corredor', 'tipo_red', 'carriles', 'cuerpos']
    search_fields = ['nombre', 'carretera']

class SubtramoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'tramo']}),
        (u'Caracter\u00edsticas', {'fields': ['km_inicio', 'km_fin']}),
        (u'Geo Ubicaci\u00f3n', {
            'fields': ['latitud_inicio', 'longitud_inicio', 'latitud_fin', 'longitud_fin'],
            'classes': ['collapse']
        }),
    ]
    list_display = ('nombre', 'tramo', 'km_inicio', 'km_fin')
    list_filter = ['tramo']
    search_fields = ['nombre', 'tramo']

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Corredor, CorredorAdmin)
admin.site.register(Carretera, CarreteraAdmin)
admin.site.register(Tramo, TramoAdmin)
admin.site.register(Subtramo, SubtramoAdmin)

