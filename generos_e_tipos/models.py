from django.db import models


class Generos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.nome


class Tipos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.nome
