from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from carreteras.models import *
from carreteras.commons import *

def index(request):
    return render_to_response('carreteras/index.html', {
        'title': 'Buscador de carreteras',
        'MEDIA_URL': settings.MEDIA_URL,
        'estados': ESTADOS_CHOICES,
    })

