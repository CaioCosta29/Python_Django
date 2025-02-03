from django.urls import path
from galeria.views import index, imagem, buscar_input

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id_foto>', imagem, name='imagem'),
    path('buscar', buscar_input, name='buscar_input'),
]