from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField



class Categoria(models.Model):
    nome = models.CharField(u'Categoria:', max_length=100, unique=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        permissions = (
            ('usuario_categoria_add', 'Pode Adicionar Categoria'),
            ('usuario_categoria_edit', 'Pode Editar Categoria'),
        )
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Post(models.Model):
    STATUS_CHOICES = (
        ('1', 'ONLINE'),
        ('2', 'RASCUNHO'),
    )
    titulo = models.CharField(u'Titulo:', max_length=150, blank=False)
    slug = models.SlugField(u'Slug:', max_length=255, unique=True)
    resumo = models.CharField(u'Resumo:', max_length=255, blank=True, null=True)
    content = HTMLField(u'Conteudo:', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,  null=True, verbose_name='Autor:')
    categoria = models.ManyToManyField(Categoria, blank=True, verbose_name='Categoria:')
    status = models.CharField(u'Status:', max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        permissions = (
            ('usuario_post_add', 'Pode Adicionar Post'),
            ('usuario_post_edit', 'Pode Editar Post'),
        )
        ordering = ['date_created']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo