from django import forms
from django.forms import DateInput
from .models import Venda
from produtos.models import Produto

class VendaForm(forms.ModelForm):
    data = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data da Venda'
    )

    class Meta:
        model = Venda
        fields = ['produto', 'data', 'quantidadeProduto', 'valorTotal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'produto' in self.data:
            try:
                produto_id = int(self.data.get('produto'))
                produto = Produto.objects.get(id=produto_id)
                self.fields['quantidadeProduto'].widget.attrs['max'] = produto.quantidade
            except (ValueError, Produto.DoesNotExist):
                pass
