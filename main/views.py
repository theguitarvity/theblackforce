from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# cria uma requisição para a api, requerindo os filmes da franquia
response = requests.get('https://swapi.co/api/films')


#armazena o json da requisição
data = response.json()

#view index lista todos os filmes da franquia
def index(request):   
    context = {'films_list':data['results']}
    return render(request,'main/home.html', context)

# view detail lista as caracteristicas do filme
def detail(request, episode_id):
    
    #seleciona o filme pelo id
    context = {'film_item:':data['results'][episode_id]}

    
    return render(request, 'main/detail.html', context)