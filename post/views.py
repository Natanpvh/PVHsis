from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from post.forms import RegisterPostForm, EditaPostForm, RegisterCategoriaForm
from post.models import Post, Categoria


@login_required
def home(request):
    template = 'dashboard/content.html'
    usuario = User.objects.all().count()
    post = Post.objects.all()
    total_post_offline = post.filter(status=2).count()
    total_post_online = post.filter(status=1).count()
    categorias = Categoria.objects.all().count()
    context = {
        'usuario': usuario,
        'offline': total_post_offline,
        'online': total_post_online,
        'categorias': categorias,
    }

    return render(request, template, context)


@login_required
def listar_post(request):
    """ Lista Posts """
    template = 'posts.html'

    if 'q' in request.GET != False:
        # SE for buscar
        if request.user.is_staff:
            post_busca = Post.objects.all().order_by('-id')

            busca = request.GET.get("q")
            post_list = post_busca.filter(
                Q(titulo__icontains=busca)|
                Q(autor__username=busca)|
                Q(categoria__nome=busca)
            )

        else:
            post_busca = Post.objects.filter(autor=request.user.id).order_by('-id')

            busca = request.GET.get("q")
            post_list = post_busca.filter(
                Q(titulo__icontains=busca) |
                Q(categoria__nome=busca)
            )

        total_post = post_list.count()
        total_post_online = post_list.filter(status=1).count()

        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 2)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)

        context = {
            'total': total_post,
            'online': total_post_online,
            'post': post,
        }
        return render(request, template, context)

    else:

        if request.user.is_staff:
            post_list = Post.objects.all().order_by('-id')
        else:
            post_list = Post.objects.filter(autor=request.user.id).order_by('-id')

        total_post = post_list.count()
        total_post_online = post_list.filter(status=1).count()

        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 2)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)

        context = {
            'total': total_post,
            'online': total_post_online,
            'post': post,
        }
        return render(request, template, context)


@login_required
@permission_required('post.usuario_post_add', raise_exception=True)
def cadastrar_post(request):
    """ Cadastra o Post"""
    template_name = 'post_form.html'
    nome_temp = 'Cadastrar'
    if request.method == 'POST':
        form = RegisterPostForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Cadastrado com Sucesso!')
            return HttpResponseRedirect(reverse('posts'))
    else:
        form = RegisterPostForm()
    context = {
        'titulo_pagina': nome_temp,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
@permission_required('post.usuario_post_edit', raise_exception=True)
def atualiza_post(request, pk):
    """ Edida o Post"""
    template_name = 'post_form.html'
    nome_temp = 'Atualizar'
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = EditaPostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            post_titulo = form.cleaned_data.get('titulo')
            messages.success(request, 'O Post >> {} << foi atualizado com Sucesso!'.format(post_titulo))
            return HttpResponseRedirect(reverse('posts'))

    else:
        form = EditaPostForm(instance=post)
    context = {
        'titulo_pagina2': nome_temp,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
@permission_required('post.usuario_categoria_edit')
def listar_categoria(request):
    """ Lista Posts """
    template = 'categorias.html'
    categoria = Categoria.objects.all()
    total_categoria = categoria.count()

    context = {
        'total': total_categoria,
        'category': categoria,
    }
    return render(request, template, context)


@login_required
@permission_required('post.usuario_categoria_add', raise_exception=True)
def cadastrar_categoria(request):
    """ Cadastra Categoria"""
    template_name = 'cadastrar_categoria.html'
    if request.method == 'POST':
        form = RegisterCategoriaForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria Cadastrada com Sucesso!')
            return HttpResponseRedirect(reverse('category'))
    else:
        form = RegisterCategoriaForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
