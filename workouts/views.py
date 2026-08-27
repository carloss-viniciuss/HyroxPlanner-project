from django.shortcuts import render, redirect # Adicionado redirect
from .models import Treino, Competicao
from .forms import TreinoForm # Importa o formulário

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
