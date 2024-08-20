from django import forms
from django.forms import DateInput
from .models import Compra

class CompraForm(forms.ModelForm):
    data = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data'
    )

    class Meta:
        model = Compra
        fields = ['nome', 'valorUnidade', 'valorTotal', 'data', 'fornecedor', 'quantidade']
