from django.db import models


class Despesa(models.Model):
    
    ESCOLHAS_NATUREZA = [
        ('vendedor', 'Vendedor'),
        ('caixa', 'Caixa'),
        ('administrador','Administrador')
    ]

    nome = models.CharField(max_length=255)  # Especificando o tipo de campo e tamanho máximo
    descricao = models.TextField()  # Usando TextField para descrições mais longas
    data = models.DateField()
    natureza = models.CharField(max_length=20, choices=ESCOLHAS_NATUREZA, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return str(self.despesa) + " / ID: " + str(self.id)
