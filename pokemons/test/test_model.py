from django.test import TestCase, RequestFactory
from pokemons.models import Pokemon

class PokemonModelTestCase(TestCase):
    
    def setUp(self):
        self.pokemon = Pokemon.objects.create(
            nome_pokemon = 'charmander',
            type_fire = 'Sim',
            type_poison = 'Não',
            domestic = 'Não'
        )

    def test_pokemon_cadastrado_com_caracteristicas(self):
        """teste que verifica se o pokemon está cadastrado com suas caracteristicas"""
        self.assertEqual(self.pokemon.nome_pokemon, 'charmander')