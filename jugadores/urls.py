from django.urls import path
from .views import lista_jugadores
from .views import agregar_jugador

urlpatterns = [
    path('', lista_jugadores, name='lista_jugadores'),
    path('agregar/', agregar_jugador, name='agregar_jugador'),
    
]
