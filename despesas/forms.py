from django import forms
from django.forms import DateInput
from .models import Despesa


class DespesasForm(forms.ModelForm):
    data = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data da Despesa'
    )

    class Meta:
        model = Despesa
        fields = ['nome', 'descricao', 'data', 'natureza', 'valor']
