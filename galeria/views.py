from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.filter(status_publicado=True)
    return render(request, 'index.html', {"cards": fotografias})


def imagem(request, id_foto):
    foto = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, 'imagem.html', {'foto': foto})

def buscar_input(request):
    fotografias = Fotografia.objects.filter(status_publicado=True)

    buscar = request.GET.get('buscar_input', '')

    if buscar: 
        fotografias = fotografias.filter(nome__icontains=buscar)
    

    return render(request, 'buscar.html', {"cards": fotografias})
