from django.test import TestCase

from carreteras import encoders
from carreteras.models import Carretera, Ruta

import simplejson as json

# Decode json to a list of carreteras
def as_carretera_list(dct):
    if 'carreteras' in dct:
        carreteras = []
        for c in dct['carreteras']:
            carretera = Carretera(pk=c['id'],
                identificador_nacional=c['identificador_nacional'],
                nombre=c['nombre'], ruta=as_ruta(c['ruta']))
            carreteras.append(carretera)
        return carreteras
    return dct

# Decode json to a ruta
def as_ruta(dct):
    return Ruta(pk=dct['id'], numero=dct['numero'], nombre=dct['nombre'])

class EncodersTestCase(TestCase):
    def setUp(self):
        self.r1 = Ruta(pk=1, numero=80, nombre='Ruta Ochenta')
        self.r2 = Ruta(pk=2, numero=81, nombre='Ruta Ochenta y uno')
        self.c1 = Carretera(pk=1, identificador_nacional='100',
                nombre='Mexico-Puebla', ruta=self.r1)
        self.c2 = Carretera(pk=2, identificador_nacional='101',
                nombre='Mexico-Cuernavaca', ruta=self.r2)
        self.carreteras = [self.c1, self.c2]

class CarreteraToDictMethod(EncodersTestCase):
    def test_should_convert_carretera_to_dict(self):
        carretera = encoders.carreteraToDict(self.c1)
        self.assertEqual(carretera['id'], self.c1.pk)
        self.assertEqual(carretera['identificador_nacional'],
                self.c1.identificador_nacional)
        self.assertEqual(carretera['nombre'], self.c1.nombre)
        ruta = carretera['ruta']
        self.assertEqual(ruta['id'], self.r1.pk)
        self.assertEqual(ruta['label'], 'MEX-' + str(self.r1.numero))
        self.assertEqual(ruta['numero'], self.r1.numero)
        self.assertEqual(ruta['nombre'], self.r1.nombre)

class CarreterasToJsonMethod(EncodersTestCase):
    def test_should_return_valid_json(self):
        json_string = encoders.carreterasToJson(self.carreteras)
        # JSONDecodeError if json_string is not valid json
        json.loads(json_string)

    def test_should_specify_the_number_of_results(self):
        json_string = encoders.carreterasToJson(self.carreteras)
        decoded = json.loads(json_string)
        self.assertEqual(decoded['success'], True)
        self.assertEqual(decoded['results'], 2)
        self.assertEqual(decoded['results'], len(decoded['carreteras']))

    def test_should_contain_a_list_of_carreteras(self):
        json_string = encoders.carreterasToJson(self.carreteras)
        carreteras = json.loads(json_string, object_hook=as_carretera_list)
        self.assertEquals(len(carreteras), 2)
        self.assertIsInstance(carreteras[0], Carretera)
        self.assertIsInstance(carreteras[0].ruta, Ruta)
