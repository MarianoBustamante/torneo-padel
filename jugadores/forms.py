from django import forms
from .models import Jugador
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'categoria', 'edad']

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if categoria not in dict(Jugador.CATEGORIAS):
            raise forms.ValidationError("Categoría inválida.")
        return categoria

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return edad

class CustomAuthenticationForm(AuthenticationForm):
    # Si deseas agregar validaciones personalizadas, puedes hacerlo aquí.
    pass

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Validación para asegurarse de que el nombre de usuario no contenga espacios
        if ' ' in username:
            raise forms.ValidationError("El nombre de usuario no puede contener espacios.")

        # Validación para asegurarse de que el nombre de usuario sea único
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso, elige otro.")

        return username
