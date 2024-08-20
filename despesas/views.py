from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Despesa
from MPEs.utils import create_groups
from django.shortcuts import render
from .forms import DespesasForm




@login_required
def create(request):
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/despesas/?msg=Salvo')
    else:
        form = DespesasForm()

    return render(request, "despesas/formDespesas.html", {'form': form})

@login_required
def editar(request, id_despesa):

    despesa = Despesa.objects.get(pk=id_despesa)

    if request.method == 'POST':
        form = DespesasForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/despesas/?msg=Salvo')
    else:
        form = DespesasForm(instance=despesa)

    return render(request, "despesas/updateDespesas.html", {'form': form, 'id_despesa': id_despesa})

@login_required
def listartudo(request):
    create_groups()
    user = request.user.username
    despesa = Despesa.objects.all()

    return render(request, "despesas/listartudo.html", {'despesa': despesa, 'user':user })

@login_required
def deletar(request,id_despesa):
    despesa = Despesa.objects.get(pk=id_despesa).delete()

    return HttpResponseRedirect('/despesas/?msg=Excluido')

@login_required
def confirmarExcluir(request,id_despesa):
    despesa =Despesa.objects.get(pk=id_despesa)

    return render(request, "despesas/confirmarExcluir.html", {'despesa': despesa})

@login_required
def detail(request, id_despesa):

    try:
        saida =  Despesa.objects.get(pk=id_despesa)
    except:
        saida = "Sem nenhum gasto salvo"

    return render(request, "despesa/index.html", {'Gasto': saida})

    

