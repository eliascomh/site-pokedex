from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from pokemons.models import Pokemon

class PokemonTestCase(LiveServerTestCase):
    
    def setUp(self):                
        self.browser = webdriver.Firefox('/home/eliascomh/Documents/projetos_django/tdd_busca_pokemon/')
        self.pokemon = Pokemon.objects.create(
            nome_pokemon = 'charmander',
            type_fire = 'Sim',
            type_poison = 'Não',
            domestic = 'Não'
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_pokemon(self):
        """testando se um usuário encontra um pokémon na pesquisa"""
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Pokémon', brand_element.text)
        buscar_pokemon_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-pokemon')
        self.assertEqual(buscar_pokemon_input.get_attribute('placeholder'), 'Exemplo: charmander, bulbasaur')
        buscar_pokemon_input.send_keys('charmander')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        type_pokemon = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(type_pokemon), 3)