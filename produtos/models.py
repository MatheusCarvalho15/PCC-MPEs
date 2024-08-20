from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    unidadeMedida = models.CharField(max_length=20)
    codDeBarra = models.CharField(max_length=50)
    valorVenda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valorCompra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome