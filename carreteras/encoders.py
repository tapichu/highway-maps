import simplejson as json

def carreteraToDict(carretera):
    return {
        'id': carretera.pk,
        'nombre': carretera.nombre,
        'identificador_nacional': carretera.identificador_nacional,
        'ruta': {
            'id': carretera.ruta.pk,
            'label': str(carretera.ruta),
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

def tramoToDict(tramo):
    return {
        'id': tramo.pk,
        'nombre': tramo.nombre,
        'estados': [estado.nombre for estado in tramo.estados.all()],
        'municipios': [municipio.nombre for municipio in tramo.municipios.all()],
        'localidad': tramo.localidad.nombre,
        'corredor': tramo.corredor and str(tramo.corredor) or '',
        'tipo_red': tramo.tipo_red,
        'km_inicio': float(str(tramo.km_inicio)),
        'km_fin': float(str(tramo.km_fin)),
        'longitud': tramo.longitud(),
        'carriles': tramo.carriles,
        'cuerpos': tramo.cuerpos,
        'origen': tramo.origen,
        'destino': tramo.destino,
        'latitud_inicio': float(str(tramo.latitud_inicio)),
        'longitud_inicio': float(str(tramo.longitud_inicio)),
        'latitud_fin': float(str(tramo.latitud_fin)),
        'longitud_fin': float(str(tramo.longitud_fin))
    }

def detalleCarreteraToJson(carretera):
    response = carreteraToDict(carretera)
    response['tramos'] = [tramoToDict(tramo) for tramo in carretera.tramos.all()]
    return json.dumps(response)

