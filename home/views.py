from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def projetos(request):
    return render(request, 'projetos.html')

def sobre(request):
    return render(request, 'sobre.html')

def habilidades(request):
    return render(request, 'habilidades.html')