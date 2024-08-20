from django.db import models
from produtos.models import Produto
from django.core.exceptions import ValidationError

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    quantidadeProduto = models.PositiveIntegerField()
   
    def clean(self):
        if self.quantidadeProduto > self.produto.quantidade:
            raise ValidationError(f'Quantidade insuficiente no estoque. Disponível: {self.produto.quantidade}')

    def save(self, *args, **kwargs):
        self.clean()
        self.produto.quantidade -= self.quantidadeProduto
        self.produto.save()
        super().save(*args, **kwargs)
    
    def lucro(self):
        # Calcular o valor unitário de venda
        valor_unitario_venda = self.valorTotal / self.quantidadeProduto
        
        # Calcular o lucro por unidade
        lucro_por_unidade = valor_unitario_venda - self.produto.valorCompra
        
        # Calcular o lucro total
        return lucro_por_unidade * self.quantidadeProduto
    

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidadeProduto} unidades'

