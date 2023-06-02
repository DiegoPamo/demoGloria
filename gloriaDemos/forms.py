from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Formulario de registro de usuario
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1","password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            form.save()
        return user