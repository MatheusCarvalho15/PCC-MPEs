from django.contrib.auth.models import User
from django.db import models

class Usuario(User):

    ESCOLHAS_CARGO = [
        ('vendedor', 'Vendedor'),
        ('caixa', 'Caixa'),
        ('administrador','Administrador')
    ]

    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cargo = models.CharField(max_length=20, choices=ESCOLHAS_CARGO, blank=True, null=True)
