from django.db import models
from django.contrib.auth.models import User

class Meta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    data = models.DateField() 
    despesa = models.DecimalField(max_digits=15, decimal_places=2)  # Campo para o valor de despesas
    venda = models.DecimalField(max_digits=15, decimal_places=2)  # Campo para o valor de vendas

