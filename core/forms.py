from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User, Group
from django.forms import TextInput, EmailInput, CheckboxInput, SelectMultiple, PasswordInput


class RegisterUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff']
        widgets = {
            'username': TextInput(attrs={'class': u'form-control'}),
            'first_name': TextInput(attrs={'class': u'form-control'}),
            'last_name': TextInput(attrs={'class': u'form-control'}),
            'email': EmailInput(attrs={'class': u'form-control'}),
            'is_active': CheckboxInput(attrs={'class': u'form-check-input'}),
            'is_staff': CheckboxInput(attrs={'class': u'form-check-input'}),
            'groups': SelectMultiple(attrs={'class': u'form-control'}),
            'password1': PasswordInput(attrs={'class': u'form-control'}),
            'password2': PasswordInput(attrs={'class': u'form-control'}),
        }


class EditUsuarioForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',
                  'groups']

        widgets = {
            'username': TextInput(attrs={'class': u'form-control'}),
            'first_name': TextInput(attrs={'class': u'form-control'}),
            'last_name': TextInput(attrs={'class': u'form-control'}),
            'email': EmailInput(attrs={'class': u'form-control'}),
            'is_active': CheckboxInput(attrs={'class': u'form-check-input'}),
            'is_staff': CheckboxInput(attrs={'class': u'form-check-input'}),
            'is_superuser': CheckboxInput(attrs={'class': u'form-check-input'}),
            'groups': SelectMultiple(attrs={'class': u'form-control'}),
            'password': TextInput(attrs={'class': u'form-control'}),
        }


class RegisterGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

        widgets = {
            'name': TextInput(attrs={'class': u'form-control'}),
            'permissions': SelectMultiple(attrs={'class': u'form-control'}),
        }


class EditGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

        widgets = {
            'name': TextInput(attrs={'class': u'form-control'}),
            'permissions': SelectMultiple(attrs={'class': u'form-control'}),
        }

class EditPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']