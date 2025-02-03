from django.db import models

class Fotografia(models.Model):

    opcoes_categoria = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=20, choices=opcoes_categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    caminho_foto = models.ImageField(upload_to="fotos", blank=True)
    status_publicado = models.BooleanField(default=False)

