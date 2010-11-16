from django.conf.urls.defaults import *

urlpatterns = patterns('carreteras.views',
    (r'^$', 'index'),
    (r'^search/estado/(?P<estado>\w+)$', 'searchEstado'),
)
