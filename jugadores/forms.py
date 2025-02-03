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
