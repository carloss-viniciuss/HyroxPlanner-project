from django import forms
from .models import Treino, Competicao

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'tipo', 'data', 'duracao', 'intensidade']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class CompetForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome','categoria','data','local']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }