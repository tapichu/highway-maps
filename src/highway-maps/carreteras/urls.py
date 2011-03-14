from django.conf.urls.defaults import *

urlpatterns = patterns('carreteras.views',
    (r'^$', 'index'),
    (r'^carretera/(?P<id_carretera>\d+)$', 'detalleCarretera'),
    (r'^search/carretera/(?P<carretera>\w+)$', 'searchCarretera'),
    (r'^search/estado/(?P<estado>\w+)$', 'searchEstado'),
    (r'^search/localidad/(?P<localidad>\w+)$', 'searchLocalidad'),
    (r'^search/municipio/(?P<municipio>\w+)$', 'searchMunicipio'),
    (r'^search/ruta/(?P<ruta>\d+)$', 'searchRuta'),
)
