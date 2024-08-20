from django.db import models

class Compra(models.Model):
    nome = models.CharField(max_length=255)
    valorUnidade = models.DecimalField(max_digits=10, decimal_places=2)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    fornecedor = models.CharField(max_length=255)
    quantidade = models.IntegerField()


