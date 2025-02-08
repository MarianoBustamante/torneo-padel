from django import template

register = template.Library()

@register.filter
def get_categoria_display(categorias, clave):
    """Devuelve el nombre de la categoría desde el diccionario, asegurando que clave sea string"""
    return categorias.get(str(clave), "Desconocida")  # Convertimos clave a string
