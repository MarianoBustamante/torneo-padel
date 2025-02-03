from django.db import models


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad= models.IntegerField()
    categoria = models.CharField(max_length=50, choices=[
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanazado','Avanzado')
    ])
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __ster__(self):
        return f"{self.nombre} ({self.categoria})"