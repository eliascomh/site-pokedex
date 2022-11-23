from django.test import TestCase, RequestFactory
from django.urls import reverse
from pokemons.views import index

class PokemonsURLSTestCase(TestCase):

    def setUp(self):
        self.factoy = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """test se a home utiliza a função index da view"""
        request = self.factoy.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)