from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Meta
from MPEs.utils import create_groups, group_required
from django.shortcuts import render
from .forms import MetaForm
from MPEs.utils import create_groups


@group_required('administrador')
@login_required
def create(request):
    if request.method == 'POST':
        form = MetaForm(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.usuario = request.user
            form.save()
            return HttpResponseRedirect('/meta/?msg=Salvo')
    else:
        form = MetaForm()

    return render(request, "MetaLucro/formMeta.html", {'form': form})

@group_required('administrador')
@login_required
def editar(request, id_meta):
    meta = Meta.objects.get(pk=id_meta)

    if request.method == 'POST':

        form = MetaForm(request.POST, instance=meta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/meta/?msg=Salvo')
    else:
        form = MetaForm(instance=meta)

    return render(request, "MetaLucro/updatemeta.html", {'form': form, 'id_meta': id_meta})


@login_required
def listartudo(request):
    create_groups()
    user = request.user.username
    meta = Meta.objects.all()

    return render(request, "MetaLucro/listartudo.html", {'meta': meta, 'user':user })

@group_required('administrador')
@login_required
def deletar(request,id_meta):
    meta = Meta.objects.get(pk=id_meta).delete()

    return HttpResponseRedirect('/meta/?msg=Excluido')

@group_required('administrador')
@login_required
def confirmarExcluir(request,id_meta):
    meta = Meta.objects.get(pk=id_meta)

    return render(request, "MetaLucro/confirmarExcluir.html", {'meta': meta})



    
