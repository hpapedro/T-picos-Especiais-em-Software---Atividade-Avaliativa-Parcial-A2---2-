from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('senha/', views.trocar_senha, name='trocar_senha'),
    path('kanban/', views.kanban, name='kanban'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('tarefas/<int:pk>/atualizar-status/', views.atualizar_status_tarefa, name='atualizar_status_tarefa'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
