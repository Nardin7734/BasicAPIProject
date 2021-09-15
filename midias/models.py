from django.db import models
from generos_e_tipos.models import Generos, Tipos


class Midias(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)
    lancamento = models.DateField()
    nota = models.IntegerField()
    descricao = models.TextField(blank=True)
