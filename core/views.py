from django.contrib import auth, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from core.forms import RegisterUsuarioForm, EditUsuarioForm, RegisterGroup, EditGroup, EditPasswordForm


#@login_required
def listar_usuario(request):
    """ Lista Usuarios Cadastrados"""
    template = 'usuarios.html'
    if request.user.is_staff:
        usuario_sis = User.objects.all()
    else:
        usuario_sis = User.objects.filter(pk=request.user.id)

    context = {
        'user': usuario_sis
    }
    return render(request, template, context)


#@login_required
def ver_usuario(request, pk):
    """ Visualiza as descrições do Usuário"""
    usuario = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == "GET":
        context = {
            "usuario": usuario
        }
        data['html_usuario'] = render_to_string('ver_usuario.html', context, request=request)
    return JsonResponse(data)


#@login_required
def cadastro_usuario(request):
    """ Cadastra o Usuario"""
    template_name = 'cadastro_usuario.html'
    if request.method == 'POST':
        form = RegisterUsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Cadastrado de {} registrado com Sucesso!'.format(username))
            return HttpResponseRedirect(reverse('lista_usu'))
    else:
        form = RegisterUsuarioForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


#@login_required
def atualiza_usuario(request, pk):
    """ Edida o Usuario"""
    template_name = 'cadastro__edit_usuario.html'
    usuario = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = EditUsuarioForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Cadastrado de {} foi atualizado com Sucesso!'.format(username))
            return HttpResponseRedirect(reverse('lista_usu'))

    else:
        form = EditUsuarioForm(instance=usuario)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def delet_usuario(request, pk):
    """ Deleta Usuario do Sistema"""
    template_name = 'deleta_usu.html'
    usuario = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, 'Usuario deletado com Sucesso!')
        return HttpResponseRedirect(reverse('lista_usu'))

    else:
        context = {
            "usuario": usuario
        }
        return render(request, template_name, context)


@login_required
@staff_member_required(login_url="/sis/accounts/login/")
def lista_grupos(request):
    """Lista os Grupos disponiveis"""
    template_name = 'grupos.html'
    form = Group.objects.all()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def cadastro_grupo(request):
    """ Cadastra o Grupo"""
    template_name = 'cadastro_grupo.html'
    if request.method == 'POST':
        form = RegisterGroup(request.POST or None)
        if form.is_valid():
            form.save()
            group_name = form.cleaned_data.get('name')
            messages.success(request, 'Cadastrado de {} registrado com Sucesso!'.format(group_name))
            return HttpResponseRedirect(reverse('lista_grupo'))
    else:
        form = RegisterGroup()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def atualiza_grupo(request, pk):
    """ Edida o Groups"""
    template_name = 'cadastro_grupo.html'
    grupo = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        form = EditGroup(request.POST or None, instance=grupo)
        if form.is_valid():
            form.save()
            gruponame = form.cleaned_data.get('name')
            messages.success(request, 'Cadastrado de {} foi atualizado com Sucesso!'.format(gruponame))
            return HttpResponseRedirect(reverse('lista_grupo'))

    else:
        form = EditGroup(instance=grupo)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def delet_grupo(request, pk):
    """ Deleta Grupo do Sistema"""
    template_name = 'deleta_grupo.html'
    grupouser = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        grupouser.delete()
        messages.success(request, 'O Grupo foi apagado com Sucesso!')
        return HttpResponseRedirect(reverse('lista_grupo'))

    else:

        context = {
            "grupo": grupouser
        }
        return render(request, template_name, context)


def edit_password(request):
    """ Edida o Usuario"""
    template_name = 'registration/password_reset_form.html'

    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'A senha do Usuario foi auterada com Sucesso!')
            return HttpResponseRedirect(reverse('lista_usu'))

    else:
        form = EditPasswordForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)


def usu_login(request):
    template = 'login.html'
    if request.user.is_authenticated == True:
        return redirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, template)


@login_required
def usu_logout(request):
    auth.logout(request)
    return redirect('login_uso')
