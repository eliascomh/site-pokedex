from django.shortcuts import render
from pokemons.models import Pokemon

def index(request):
    context = {'caracteristicas': Pokemon.objects.all()}
    return render(request, 'index.html', context)