from django.db import models

from django.db import models

class Treino(models.Model):
    nome = models.CharField(max_length=100)        
    tipo = models.CharField(max_length=50)         
    data = models.DateField()                     
    duracao = models.CharField(max_length=50)
    intensidade = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.nome} - {self.data}"


class Competicao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    local = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
