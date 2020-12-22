from .models import *
from django import forms
class SignUpUserForm(forms.ModelForm):
    class Meta():
        model = SignUpUser
        fields = ['username', 'email', 'confirm_email', 'password', 'confirm_password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'confirm_email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
class SignInUserForm(forms.ModelForm):
    class Meta():
        model = SignInUser
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
class ChangeThePasswordForm(forms.ModelForm):
    class Meta():
        model = ChangePassword
        fields = ['current_password', 'new_password', 'confirm_new_password']
        widgets = {
            'current_password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'new_password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_new_password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
