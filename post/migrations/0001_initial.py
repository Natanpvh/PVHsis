# Generated by Django 2.2.4 on 2019-08-14 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Categoria:')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'permissions': (('usuario_categoria_add', 'Pode Adicionar Categoria'), ('usuario_categoria_edit', 'Pode Editar Categoria')),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo:')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug:')),
                ('resumo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Resumo:')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Conteudo:')),
                ('status', models.CharField(blank=True, choices=[('1', 'ONLINE'), ('2', 'RASCUNHO')], max_length=1, null=True, verbose_name='Status:')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor:')),
                ('categoria', models.ManyToManyField(blank=True, to='post.Categoria', verbose_name='Categoria:')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['date_created'],
                'permissions': (('usuario_post_add', 'Pode Adicionar Post'), ('usuario_post_edit', 'Pode Editar Post')),
            },
        ),
    ]
