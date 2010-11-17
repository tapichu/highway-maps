from django.conf.urls.defaults import *

urlpatterns = patterns('carreteras.views',
    (r'^$', 'index'),
    (r'^search/estado/(?P<estado>\w+)$', 'searchEstado'),
    (r'^search/localidad/(?P<localidad>\w+)$', 'searchLocalidad'),
    (r'^search/municipio/(?P<municipio>\w+)$', 'searchMunicipio'),
)
