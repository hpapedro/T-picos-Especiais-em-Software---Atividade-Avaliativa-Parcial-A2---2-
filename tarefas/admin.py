from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criador', 'atribuido_a', 'criado_em')
    list_filter = ('status', 'criador', 'atribuido_a')
    search_fields = ('titulo', 'descricao')
