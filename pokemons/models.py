from django.db import models

class Pokemon(models.Model):
    nome_pokemon = models.CharField(max_length=20)
    type_fire = models.CharField(max_length=5)
    type_poison = models.CharField(max_length=5)
    domestic = models.CharField(max_length=5)

    def __str__(self):
        return self.nome_pokemon