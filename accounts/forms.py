from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.forms import DateInput
from django.core.validators import RegexValidator

class UsuariosForm(UserCreationForm):
    data_nascimento = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data de Nascimento'
    )
    cpf = forms.CharField(
        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', 'Digite um CPF válido no formato XXX.XXX.XXX-XX')],
        label='CPF'
    )

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'data_nascimento', 'cpf', 'password1']

class UsuarioEdit(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data de Nascimento'
    )
    cpf = forms.CharField(
        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', 'Digite um CPF válido no formato XXX.XXX.XXX-XX')],
        label='CPF'
    )

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'data_nascimento', 'cpf']

class PermissionForm(forms.ModelForm):
    VENDEDOR = 'vendedor'
    CAIXA = 'caixa'
    ADMINISTRADOR = 'administrador'
    CHOICES = [
        (VENDEDOR, 'Vendedor'),
        (CAIXA, 'Caixa'),
        (ADMINISTRADOR, 'Administrador')
    ]

    cargo = forms.ChoiceField(
        label='Cadastrar:',
        choices=CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Usuario
        fields = ['cargo']
