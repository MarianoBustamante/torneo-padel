from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'categoria', 'edad']

    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if categoria not in dict(Jugador.CATEGORIAS):
            raise forms.ValidationError("Categoría inválida.")
        return categoria

# jugadores/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clases de Bootstrap a los campos del formulario
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
