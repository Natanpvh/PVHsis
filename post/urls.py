"""PVHsis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from post import views

urlpatterns = [

    # Dashboard do Sistema
    path('', views.home, name='index'),

    # Posts
    path('sis/post/', views.listar_post, name='posts'),
    path('sis/post/cadastrar/', views.cadastrar_post, name='cadastra_post'),
    path('sis/post/edit/<int:pk>/', views.atualiza_post, name='editar_post'),

    # Categorias
    path('sis/categorias/', views.listar_categoria, name='category'),
    path('sis/categorias/cadastrar/', views.cadastrar_categoria, name='cadastra_category'),
    path('sis/post/edit/<int:pk>/', views.atualiza_post, name='editar_post'),

]
