from django.contrib import admin
from galeria.models import Fotografia

class listar_fotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "status_publicado")
    search_fields = ("nome",)
    list_editable = ("status_publicado",)

admin.site.register(Fotografia, listar_fotografia)