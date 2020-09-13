from django.contrib.auth.forms import *
from .models import Usuario


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'celular')
        labels = {'username': 'e-mail'}

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password1'])
        usuario.email = self.cleaned_data['username']
        if commit:
            usuario.save()
        return usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'celular')
