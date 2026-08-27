from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_treinos, name='visualizar_treinos'),
    path('novo/', views.criar_treino, name='adicionar_treino'),
    path('competicoes/', views.listar_competicoes, name='visualizar_competicoes'),
    path('competicoes/nova/', views.criar_competicao, name='criar_competicao'),
]