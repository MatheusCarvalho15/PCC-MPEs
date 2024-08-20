from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import redirect
from MPEs.utils import group_required



@group_required('caixa, administrador')
@login_required
def criarProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()

            # Verifica se o produto já existe
            produto_existente = Produto.objects.filter(
                nome=produto.nome,
                valorCompra=produto.valorCompra
            ).first()

            if produto_existente:
                # Atualiza a quantidade do produto existente
                produto_existente.quantidade += produto.quantidade
                produto_existente.save()
            else:
                # Cria um novo produto
                Produto.objects.create(
                    nome=produto.nome,
                    valorCompra=produto.valorCompra,
                    quantidade=produto.quantidade
                )

            return redirect('listarProduto')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/formProdutos.html', {'form': form})


@group_required('caixa, administrador')
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


@group_required('caixa, administrador')
@login_required
def listarProduto(request):
    user = request.user.username
    produto = Produto.objects.all()
    
    return render(request, "produtos/listarProduto.html", {'produto': produto, 'user': user})


@group_required('caixa, administrador')
@login_required
def deletar(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    produto.delete()
    
    return HttpResponseRedirect('/produtos/?msg=Excluido')


@group_required('caixa, administrador')
@login_required
def confirmarExcluir(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    
    return render(request, "produtos/confirmarExcluir.html", {'produto': produto})
