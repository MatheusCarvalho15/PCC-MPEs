from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Venda
from MPEs.utils import create_groups, group_required
from django.shortcuts import render
from .forms import VendaForm
from MPEs.utils import create_groups
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from produtos.models import Produto


@group_required('vendedor, administrador')
def create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/venda/?msg=Salvo')
    else:
        form = VendaForm()

    produto = Produto.objects.all

    return render(request, "venda/formVenda.html", {'form': form, 'produto': produto})

@group_required('vendedor, administrador')
@login_required
def editar(request, id_venda):
    venda = Venda.objects.get(pk=id_venda)

    if request.method == 'POST':

        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/venda/?msg=Salvo')
    else:
        form = VendaForm(instance=venda)
    
    produto = Produto.objects.all

    return render(request, "venda/updateVenda.html", {'form': form, 'id_venda': id_venda, 'produto': produto})

@group_required('vendedor')
@login_required
def listartudo(request):
    create_groups()
    user = request.user.username
    venda = Venda.objects.all()

    return render(request, "venda/listartudo.html", {'venda': venda, 'user':user })

@group_required('vendedor')
@login_required
def deletar(request,id_venda):
    venda = Venda.objects.get(pk=id_venda).delete()

    return HttpResponseRedirect('/venda/?msg=Excluido')

@group_required('vendedor, administrador')
@login_required
def confirmarExcluir(request,id_venda):
    venda = Venda.objects.get(pk=id_venda)

    return render(request, "venda/confirmarExcluir.html", {'venda': venda})

@group_required('vendedor, administrador')
@login_required
def detail(request, id_venda):

    try:
        saida =  Venda.objects.get(pk=id_venda)
    except:
        saida = "Sem nenhum gasto salvo"

    return render(request, "venda/index.html", {'venda': saida})

@login_required
@group_required('vendedor, administrador')
def gerar_nota_fiscalVenda(request, id_venda):
    venda = Venda.objects.get(pk=id_venda)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="nota_fiscal_venda.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(name="RightAlign", alignment=2))  # Adiciona estilo alinhado à direita
    
    elements.append(Paragraph("Nota Fiscal da Venda", styles['Title']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"Data da Venda: {venda.data.strftime('%d/%m/%Y')}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    data = [
        ["Descrição", "Valor"],
        ["Produto", venda.produto.nome],
        ["Quantidade", str(venda.quantidadeProduto)],
        ["Valor Unitário", f"R$ {venda.valorTotal / venda.quantidadeProduto:.2f}"],
        ["Valor Total", f"R$ {venda.valorTotal:.2f}"]
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