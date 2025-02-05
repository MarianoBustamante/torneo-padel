from django.db import models

class Jugador(models.Model):
    CATEGORIAS = [
        ('1ra', 'Primera'),
        ('2da', 'Segunda'),
        ('3ra', 'Tercera'),
        ('4ta', 'Cuarta'),
        ('5ta', 'Quinta'),
        ('6ta', 'Sexta'),
        ('7ma', 'Séptima'),
        ('8va', 'Octava'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='8va')
    edad = models.IntegerField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"
