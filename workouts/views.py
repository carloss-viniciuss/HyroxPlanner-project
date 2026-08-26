from django.shortcuts import render
from .models import Treino, Competicao

def listar_treinos(request):
    treinos = Treino.objects.all()

    return render(request, 'workouts/listar_treinos.html', {'treinos': treinos})

def listar_competicoes(request):
    competicoes = Competicao.objects.all()
    
    return render(request, 'workouts/listar_competicoes.html', {'competicoes': competicoes})
