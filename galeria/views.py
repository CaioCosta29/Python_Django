from django.shortcuts import render


def index(request): # acessar a pagina principal
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

