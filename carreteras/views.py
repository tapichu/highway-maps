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
    carreteras = Carretera.objects.filter(tramos__estados__nombre__exact=estado).distinct()
    data = encoders.carreterasToJson(carreteras)
    return HttpResponse(data)

