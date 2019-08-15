from django.forms import forms, TextInput, Select, SelectMultiple, RadioSelect
from django import forms
#from tinymce_4.fields import TinyMCEFormField

from post.models import Post, Categoria


class RegisterPostForm(forms.ModelForm):
   # content = forms.CharField(widget=TinyMCEFormField(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'resumo', 'content', 'autor', 'categoria', 'status']

        widgets = {
            'titulo': TextInput(attrs={'class': u'form-control'}),
            'slug': TextInput(attrs={'class': u'form-control'}),
            'resumo': TextInput(attrs={'class': u'form-control'}),
            'autor': Select(attrs={'class': u'form-control'}),
            'categoria': SelectMultiple(attrs={'class': u'form-control'}),
            'status': Select(attrs={'class': u'form-control'}),
        }


class EditaPostForm(forms.ModelForm):
   # content = forms.CharField(widget=TinyMCEFormField(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'resumo', 'content', 'autor', 'categoria', 'status']

        widgets = {
            'titulo': TextInput(attrs={'class': u'form-control'}),
            'slug': TextInput(attrs={'class': u'form-control'}),
            'resumo': TextInput(attrs={'class': u'form-control'}),
            'autor': Select(attrs={'class': u'form-control'}),
            'categoria': SelectMultiple(attrs={'class': u'form-control'}),
            'status': Select(attrs={'class': u'form-control'}),
        }


class RegisterCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

        widgets = {
            'nome': TextInput(attrs={'class': u'form-control'}),
        }
