from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from carreteras.models import *
from carreteras.commons import *
import carreteras.encoders as encoders

def index(request):
    return render_to_response('carreteras/index.html', {
        'title': 'Buscador de carreteras',
        'MEDIA_URL': settings.MEDIA_URL,
        'estados': ESTADOS_CHOICES,
    },
    context_instance=RequestContext(request))

def searchEstado(request, estado):
    estado = estado.replace('__', ' ')
    carreteras = Carretera.objects.filter(tramos__estados__nombre__exact=estado).distinct()
    data = encoders.carreterasToJson(carreteras)
    return HttpResponse(data)

def searchLocalidad(request, localidad):
    localidad = localidad.replace('__', ' ')
    carreteras = Carretera.objects.filter(tramos__localidad__nombre__contains=localidad).distinct()
    data = encoders.carreterasToJson(carreteras)
    return HttpResponse(data)

def searchMunicipio(request, municipio):
    municipio = municipio.replace('__', ' ')
    carreteras = Carretera.objects.filter(tramos__municipios__nombre__contains=municipio).distinct()
    data = encoders.carreterasToJson(carreteras)
    return HttpResponse(data)

