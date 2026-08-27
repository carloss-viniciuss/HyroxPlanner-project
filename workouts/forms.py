from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'tipo', 'data', 'duracao', 'intensidade']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }