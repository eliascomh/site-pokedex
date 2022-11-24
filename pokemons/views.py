from django.shortcuts import render
from pokemons.models import Pokemon

def index(request):
    context = {'caracteristicas': None}

    if 'buscar' in request.GET:
        pokemons = Pokemon.objects.all()
        pokemon_pesquisado = request.GET['buscar']
        caracteristicas = pokemons.filter(nome_pokemon__icontains = pokemon_pesquisado)
        context = {'caracteristicas': caracteristicas}
    return render(request, 'index.html', context)