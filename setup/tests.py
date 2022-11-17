from django.test import LiveServerTestCase
from selenium import webdriver
 
class PokemonTestCase(LiveServerTestCase):
    
    def setUp(self):                
        self.browser = webdriver.Firefox('/home/eliascomh/Documents/projetos_django/tdd_busca_pokemon/')

    def tearDown(self):
        self.browser.quit()

    def open_firefox(self):
        self.browser.get(self.live_server_url)
    
    def test_failed(self):
        """teste exemplo erro"""
        self.fail('Teste falhou')