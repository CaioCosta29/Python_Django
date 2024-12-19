from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotogafias = Fotografia.objects.all()
    return render(request, 'index.html', {"cards": fotogafias})

def imagem(request, id_foto):
    foto = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, 'imagem.html', {'foto': foto})
