from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from pokemons.models import Pokemon

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.pokemon = Pokemon.objects.create(
            nome_pokemon = 'squirtle',
            type_fire = 'Não',
            type_poison = 'Não',
            domestic = 'Sim'
            )


    def test_index_view_retorna_type_pokemon(self):
        """teste se verifica se a index retorna a caracteristica do pokemon pesquisado"""
        response = self.client.get('/', 
                {'buscar' : 'squirtle'}
            )
        type_pokemon_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(type_pokemon_pesquisado[0].nome_pokemon, 'squirtle')