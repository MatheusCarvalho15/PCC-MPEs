from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import redirect


@login_required
def criarProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProduto')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/formProdutos.html', {'form': form})

@login_required
def editar(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produtos/?msg=Salvo')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, "produtos/updateProdutos.html", {'form': form, 'id_produto': id_produto})

@login_required
def listarProduto(request):
    user = request.user.username
    produto = Produto.objects.all()
    
    return render(request, "produtos/listarProduto.html", {'produto': produto, 'user': user})

@login_required
def deletar(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    produto.delete()
    
    return HttpResponseRedirect('/produtos/?msg=Excluido')

@login_required
def confirmarExcluir(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    
    return render(request, "produtos/confirmarExcluir.html", {'produto': produto})
