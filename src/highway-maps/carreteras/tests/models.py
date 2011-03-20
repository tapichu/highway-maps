from django.test import TestCase

from carreteras.models import *

class ModelsTestCase(TestCase):
	# Load test data
	fixtures = ['test']

class EstadoTestCase(ModelsTestCase):
	def test_should_have_test_data(self):
		self.assertEqual(len(Estado.objects.all()), 32)

	def test_should_return_name_when_converted_to_string(self):
		colima = Estado.objects.filter(nombre='COLIMA')[0]
		self.assertEqual(str(colima), 'COLIMA')

class MunicipioTestCase(ModelsTestCase):
	def test_should_have_test_data(self):
		self.assertEqual(len(Municipio.objects.all()), 48)

	def test_should_return_name_when_converted_to_string(self):
		asientos = Municipio.objects.filter(nombre='Asientos')[0]
		self.assertEqual(str(asientos), 'Asientos')

	def test_should_belong_to_a_state(self):
		asientos = Municipio.objects.filter(nombre='Asientos')[0]
		self.assertIsInstance(asientos.estado, Estado)
		self.assertEqual(asientos.estado.nombre, 'AGUASCALIENTES')

class RutaTestCase(ModelsTestCase):
	def test_should_have_test_data(self):
		self.assertEqual(len(Ruta.objects.all()), 2)

	def test_should_return_code_when_converted_to_string(self):
		ruta1 = Ruta.objects.filter(numero=1)[0]
		self.assertEqual(str(ruta1), 'MEX-1')
