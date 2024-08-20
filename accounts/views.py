from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import PermissionForm
from accounts.forms import UsuariosForm, PermissionForm, UsuarioEdit
from MPEs.utils import create_groups, group_required



def register(request):
    create_groups()
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            user = form.save()  
            grupo = Group.objects.get(name='funcionario')
            grupo.user_set.add(user)
            
            return redirect('login') 
                       
    else:
        form = UsuariosForm()
    
    return render(request, 'registration/register.html', {'form': form})

@group_required(['administrador'], "/accounts/login/")
def listarUsuarios(request):
    usuario = Usuario.objects.all()

    return render(request, "registration/listarUsuarios.html", {'usuario': usuario})


@login_required
def listarDados(request):
    id_user = request.user.id
    usuario = Usuario.objects.get(pk=id_user)

    return render(request, "registration/listarDados.html", {'usuario': usuario})


@login_required
def editarDados(request, id_user):
    usuario = Usuario.objects.get(pk=id_user)

    if request.method == 'POST':

        form = UsuarioEdit(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/listarDados/?msg=Salvo')
    else:
        form = UsuarioEdit(instance=usuario)

    return render(request, "registration/updateUsuario.html", {'form': form, 'id_user': id_user})


@group_required('administrador')
def editarFunção(request, id_user):

    usuario = get_object_or_404(Usuario, pk=id_user)

    if request.method == 'POST':
  
        form = PermissionForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()

            cargo = form.cleaned_data.get('cargo')

            try:
           
                usuario.groups.clear()

         
                grupo, created = Group.objects.get_or_create(name=cargo)
                grupo.user_set.add(usuario)
            except Group.DoesNotExist:
                return HttpResponse(f"Grupo '{cargo}' não encontrado", status=404)

            return HttpResponseRedirect('/accounts/Usuarios/?msg=Salvo')
    else:
        form = PermissionForm(instance=usuario)

    return render(request, "registration/updateCargo.html", {'form': form, 'id_user': id_user})



@group_required('administrador')
def deletarUsuario(request, id_user):
    usuario = Usuario.objects.get(pk=id_user).delete()

    return HttpResponseRedirect('/despesas/?msg=Excluido')