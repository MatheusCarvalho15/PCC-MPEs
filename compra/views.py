from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Compra
from despesas.models import Despesa
from produtos.models import Produto
from MPEs.utils import create_groups, group_required
from .forms import CompraForm
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors


@group_required('vendedor')
@login_required
def create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()

            Despesa.objects.create(
                nome=compra.nome,
                data=compra.data,
                valor=compra.valorTotal,
                natureza='produto'
            )

            produto_existente = Produto.objects.filter(
                nome=compra.nome,
                valorCompra=compra.valorUnidade
            ).first()

            if produto_existente:
                produto_existente.quantidade += compra.quantidade
                produto_existente.save()
            else:
                Produto.objects.create(
                    nome=compra.nome,
                    valorCompra=compra.valorUnidade,
                    quantidade=compra.quantidade
                )

            return HttpResponseRedirect('/compra/?msg=Salvo')
    else:
        form = CompraForm()

    return render(request, "compra/formCompra.html", {'form': form})


@group_required('vendedor')
@login_required
def editar(request, id_compra):
    compra = Compra.objects.get(pk=id_compra)

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compra/?msg=Salvo')
    else:
        form = CompraForm(instance=compra)

    return render(request, "compra/updateCompra.html", {'form': form, 'id_compra': id_compra})


@group_required('vendedor')
@login_required
def listartudo(request):
    create_groups()
    user = request.user.username
    compras = Compra.objects.all()

    return render(request, "compra/listartudo.html", {'compra': compras, 'user': user})


@group_required('vendedor')
@login_required
def deletar(request, id_compra):
    Compra.objects.get(pk=id_compra).delete()
    return HttpResponseRedirect('/compra/?msg=Excluido')


@group_required('vendedor')
@login_required
def confirmarExcluir(request, id_compra):
    compra = Compra.objects.get(pk=id_compra)
    return render(request, "compra/confirmarExcluir.html", {'compra': compra})


@group_required('vendedor')
@login_required
def detail(request, id_compra):
    try:
        compra = Compra.objects.get(pk=id_compra)
    except Compra.DoesNotExist:
        compra = "Sem nenhum gasto salvo"

    return render(request, "compra/index.html", {'compra': compra})


@group_required('vendedor')
@login_required
def gerar_nota_fiscalCompra(request, id_compra):
    compra = Compra.objects.get(pk=id_compra)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="nota_fiscal_compra.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(name="RightAlign", alignment=2))  # Adiciona estilo alinhado à direita
    
    elements.append(Paragraph("Nota Fiscal da Compra", styles['Title']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"Data da Compra: {compra.data.strftime('%d/%m/%Y')}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    data = [
        ["Descrição", "Detalhe"],
        ["Produto", compra.nome],
        ["Quantidade", str(compra.quantidade)],
        ["Valor Unitário", f"R$ {compra.valorUnidade:.2f}"],
        ["Valor Total", f"R$ {compra.valorTotal:.2f}"]
    ]

    table = Table(data, colWidths=[3 * inch, 4.5 * inch])
    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    ))
    
    elements.append(table)
    doc.build(elements)
    
    return response
