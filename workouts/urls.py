from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_treinos, name='listar_treinos'),
    path('competicoes/', views.listar_competicoes, name='listar_competicoes'),
]