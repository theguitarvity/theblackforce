from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.

def index(request):
    response = requests.get('https://swapi.co/api/films')
    data = response.json()
    
    return HttpResponse(data['results'][1]['title'])