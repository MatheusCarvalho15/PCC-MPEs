from django import forms
from django.forms import DateInput
from .models import Meta

class MetaForm(forms.ModelForm):
    data = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data'
    )

    class Meta:
        model = Meta
        fields = ['data', 'despesa', 'venda']
