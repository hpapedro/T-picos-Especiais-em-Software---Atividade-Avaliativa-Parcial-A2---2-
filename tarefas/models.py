from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluido', 'Concluído'),
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_criadas')
    atribuido_a = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tarefas_atribuidas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
