from django.shortcuts import render, redirect, get_object_or_404
from .models import Treino, Competicao
from .forms import TreinoForm
from .forms import CompetForm

def listar_treinos(request):
    treinos = Treino.objects.all()
    return render(request, 'workouts/visualizar_treinos.html', {'treinos': treinos})

def listar_competicoes(request):
    competicoes = Competicao.objects.all()
    return render(request, 'workouts/visualizar_competicoes.html', {'competicoes': competicoes})

def criar_treino(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            form.save() # Grava direto no banco SQLite!
            return redirect('visualizar_treinos')
    else:
        form = TreinoForm()
    
    return render(request, 'workouts/adicionar_treino.html', {'form': form})

def criar_competicao(request):
    if request.method == 'POST':
        form = CompetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_competicoes')
    
    else:
        form = CompetForm()
        
    return render(request, 'workouts/adicionar_competicoes.html', {'form': form})

def editar_treino(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('visualizar_treinos')
    else:
        form = TreinoForm(instance=treino)
    
    return render(request, 'workouts/adicionar_treino.html', {'form': form})

def editar_competicao(request, pk):
    competicao = get_object_or_404(Competicao, pk=pk)

    if request.method == 'POST':
        form = CompetForm(request.POST, instance=competicao)
        if form.is_valid():
            form.save()
            return redirect('visualizar_competicoes')
    else:
        form = CompetForm(instance=competicao)

    return render(request, 'workouts/adicionar_competicoes.html', {'form': form})