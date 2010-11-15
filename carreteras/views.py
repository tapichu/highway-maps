from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader
from carreteras.models import *

def index(request):
    t = loader.get_template('carreteras/index.html')
    c = Context({
        'title': 'Buscador de carreteras',
        'MEDIA_URL': settings.MEDIA_URL,
    })
    return HttpResponse(t.render(c))

