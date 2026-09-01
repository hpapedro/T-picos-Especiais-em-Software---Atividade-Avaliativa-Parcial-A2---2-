import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('kanban')
    return render(request, 'tarefas/home.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('kanban')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('kanban')
    else:
        form = UserCreationForm()
    return render(request, 'tarefas/cadastro.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('kanban')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('kanban')
    else:
        form = AuthenticationForm()
    return render(request, 'tarefas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def trocar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para manter o usuário logado
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('kanban')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tarefas/trocar_senha.html', {'form': form})

@login_required
def kanban(request):
    filtro = request.GET.get('filtro', 'todas')
    
    if filtro == 'minhas':
        tarefas = Tarefa.objects.filter(atribuido_a=request.user)
    elif filtro == 'criadas':
        tarefas = Tarefa.objects.filter(criador=request.user)
    else:
        tarefas = Tarefa.objects.all()
        
    pendentes = tarefas.filter(status='Pendente')
    em_andamento = tarefas.filter(status='Em Andamento')
    concluidos = tarefas.filter(status='Concluido')
    
    context = {
        'pendentes': pendentes,
        'em_andamento': em_andamento,
        'concluidos': concluidos,
        'filtro': filtro
    }
    return render(request, 'tarefas/kanban.html', context)

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('kanban')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'acao': 'Nova'})

@login_required
def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefas/detalhe_tarefa.html', {'tarefa': tarefa})

@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('kanban')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'acao': 'Editar'})

@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.user != tarefa.criador:
        messages.error(request, 'Apenas o criador da tarefa pode excluí-la.')
        return redirect('kanban')
        
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('kanban')
    return render(request, 'tarefas/excluir_tarefa.html', {'tarefa': tarefa})

@login_required
def dashboard(request):
    total_tarefas = Tarefa.objects.count()
    tarefas_por_status = Tarefa.objects.values('status').annotate(total=Count('id'))
    tarefas_por_usuario = User.objects.annotate(
        tarefas_atribuidas_count=Count('tarefas_atribuidas')
    ).filter(tarefas_atribuidas_count__gt=0)
    
    context = {
        'total_tarefas': total_tarefas,
        'tarefas_por_status': tarefas_por_status,
        'tarefas_por_usuario': tarefas_por_usuario,
    }
    return render(request, 'tarefas/dashboard.html', context)

@login_required
@require_POST
def atualizar_status_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    try:
        data = json.loads(request.body)
        novo_status = data.get('status')
        if novo_status in dict(Tarefa.STATUS_CHOICES).keys() or novo_status in ['Pendente', 'Em Andamento', 'Concluido']:
            tarefa.status = novo_status
            tarefa.save()
            return JsonResponse({'success': True, 'status': tarefa.status})
        return JsonResponse({'success': False, 'error': 'Status inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
