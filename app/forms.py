from dataclasses import fields
import email
from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Maison 



class EnregistrementClientForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class meta:
        model = User 
        fields = ['username', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'cLass':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

class MypasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),
    strip = False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':TRUE, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})),

class Isertmaison(forms.ModelForm):
    class Meta:
        model = Maison
        fields=['title', 'Prix', 'Prix_reduit', 'description', 'quartier', 'commune', 'image_maison', 'Etat']
    


