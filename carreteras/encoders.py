import simplejson as json

def carreteraToDict(carretera):
    return {
        'pk': carretera.pk,
        'nombre': carretera.nombre,
        'identificador_nacional': carretera.identificador_nacional,
        'ruta': {
            'pk': carretera.ruta.pk,
            'id': str(carretera.ruta),
            'numero': carretera.ruta.numero,
            'nombre': carretera.ruta.nombre
        }
    }

def carreterasToJson(carreteras):
    response = {
        'success': True,
        'results': len(carreteras),
        'carreteras': [carreteraToDict(carretera) for carretera in carreteras]
    }
    return json.dumps(response)

