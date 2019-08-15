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

from core import views

urlpatterns = [

    # Cadastra Usuarios
    path('sis/user/listar', views.listar_usuario, name='lista_usu'),
    path('sis/user/cadastrar/', views.cadastro_usuario, name='cadastrar_usu'),
    path('sis/user/edit/<int:pk>/', views.atualiza_usuario, name='editar_usu'),
    path('sis/user/delete/<int:pk>/', views.delet_usuario, name='delete_usu'),
    path('sis/user/ver/<int:pk>/', views.ver_usuario, name='ver_usuario'),
    path('sis/user/edit/password/', views.edit_password, name='editar_senha'),

    # Cadastra Grupos
    path('sis/grupo/listar', views.lista_grupos, name='lista_grupo'),
    path('sis/grupo/cadastrar/', views.cadastro_grupo, name='cadastrar_grupo'),
    path('sis/grupo/edit/<int:pk>/', views.atualiza_grupo, name='editar_grupo'),
    path('sis/grupo/delete/<int:pk>/', views.delet_grupo, name='deletar_grupo'),

    # login
    path('sis/accounts/login/', views.usu_login, name='login_uso'),
    path('logout/', views.usu_logout, name='usu_logout'),


]
