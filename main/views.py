from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# cria uma requisição para a api, requerindo os filmes da franquia





#view index lista todos os filmes da franquia
def index(request):   
    try:
        response = requests.get('https://swapi.co/api/films')
        if response.status_code == 200:
            #armazena o json da requisição
            data = response.json()   
            context = {'films_list':data['results']} 
    except Exception as identifier:
        context = {'mensagem': 'Falha na conexão com a API'}
    

    return render(request,'main/home.html', context)



# view detail lista as caracteristicas do filme
def detail(request, episode_id):
    
    #seleciona o filme pelo id
    context = {'film_item:':data['results'][episode_id]}

    
    return render(request, 'main/detail.html', context)