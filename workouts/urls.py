from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_treinos, name='visualizar_treinos'),
    path('novo/', views.criar_treino, name='adicionar_treino'),
    path('editar/<int:pk>/', views.editar_treino, name='editar_treino'),

    path('competicoes/', views.listar_competicoes, name='visualizar_competicoes'),
    path('competicoes/nova/', views.criar_competicao, name='criar_competicao'),
    path('competicoes/editar/<int:pk>/', views.editar_competicao, name='editar_competicao'),

    path('deletar/<int:pk>/', views.deletar_treinos, name='deletar_treino'),
    path('competicoes/deletar/<int:pk>/', views.deletar_competicao, name='deletar_competicao'),
    
]
