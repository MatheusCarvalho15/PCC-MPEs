from django.contrib.auth.decorators import login_required
from despesas.models import Despesa
from venda.models import Venda
from metaLucro.models import Meta
from django.db.models import Sum, Max
from django.shortcuts import render
from django.db.models.functions import TruncMonth


@login_required
def home(request):
    usuario = request.user
    meta = Meta.objects.filter(usuario=usuario).order_by('-data').first()

    total_despesa = Despesa.objects.aggregate(total=Sum('valor'))['total'] or 0
    total_venda = Venda.objects.aggregate(
        total=Sum('valorTotal'))['total'] or 0
    total = total_venda - total_despesa

    dataDespesa = Despesa.objects.aggregate(
        maior_data=Max('data'))['maior_data']
    dataVenda = Venda.objects.aggregate(maior_data=Max('data'))['maior_data']

    despesas_por_mes = Despesa.objects.annotate(mes=TruncMonth('data')).values(
        'mes').annotate(total=Sum('valor')).order_by('mes')

    vendas_por_produto = Venda.objects.values('produto').annotate(
        total_venda=Sum('valorTotal')).order_by('-total_venda')

    context = {
        'meta': meta,
        'total_despesa': total_despesa,
        'total_venda': total_venda,
        'despesas_por_mes': despesas_por_mes,
        'total': total,
        'dataDespesa': dataDespesa,
        'dataVenda': dataVenda,
        'vendas_por_produto': vendas_por_produto,  # Dados para o gráfico
    }

    return render(request, 'index.html', context)
