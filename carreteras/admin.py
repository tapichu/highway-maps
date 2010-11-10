from carreteras.models import Estado, Municipio, Localidad, Ruta, Corredor, Carretera, Tramo
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

class TramoInline(admin.StackedInline):
    model = Tramo
    extra = 1

class CarreteraAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'ruta']}),
        ('IDs', {'fields': ['identificador_nacional']}),
        ('Cambios', {'fields': ['fecha_modificacion']}),
    ]
    inlines = [TramoInline]

#class TramoAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None, {'fields': ['nombre', 'carretera', 'corredor', 'origen', 'destino']}),
#        (u'Caracter\u00edsticas', {'fields': ['tipo_red', 'longitud', 'km_inicio', 'km_fin', 'carriles', 'cuerpos']}),
#    ]

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Corredor, CorredorAdmin)
admin.site.register(Carretera, CarreteraAdmin)
#admin.site.register(Tramo, TramoAdmin)

