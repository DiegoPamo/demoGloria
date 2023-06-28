from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Control_cont_neto


# Formulario de registro de usuario
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1","password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class NewControl_NetoForm(forms.ModelForm):
    linea_maq = forms.CharField(
        label = "Linea/Maquina"
    )
    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 7, "cols": 40}),
        label="Observaciones",
    )
    class Meta:
        model = Control_cont_neto
        exclude = ('sub_grupo1','sub_grupo2','sub_grupo3','sub_grupo4','sub_grupo5','promedio','rango','hora_reg',)
        # fields = '_all__'
