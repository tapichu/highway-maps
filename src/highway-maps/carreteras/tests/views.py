from django.test import TestCase

from carreteras.commons import *

import simplejson as json

class ViewsTestCase(TestCase):
	# Load test data
	fixtures = ['test']

	# Set up URLs for the tests
	urls = 'carreteras.test_urls'

class IndexView(ViewsTestCase):
	def test_should_use_index_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'carreteras/index.html')

	def test_should_have_data_in_context(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['title'], 'Buscador de carreteras')
		self.assertIsNotNone(response.context['MEDIA_URL'])
		self.assertTupleEqual(response.context['estados'], ESTADOS_CHOICES)

class SearchCarreteraView(ViewsTestCase):
	def test_should_return_json(self):
		response = self.client.get('/search/carretera/Carr')
		json.loads(response.content)

	def test_should_search_by_carretera_name(self):
		response = self.client.get('/search/carretera/Carr')
		self.assertEqual(response.status_code, 200)
		results = json.loads(response.content)
		self.assertEqual(results['success'], True)
		self.assertEqual(results['results'], 5)
		self.assertEqual(len(results['carreteras']), 5)
