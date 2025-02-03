from django.urls import path
from .views import lista_jugadores, agregar_jugador, editar_jugador, eliminar_jugador

urlpatterns = [
    path('', lista_jugadores, name='lista_jugadores'),
    path('agregar/', agregar_jugador, name='agregar_jugador'),
    path('editar/<int:jugador_id>/', editar_jugador, name='editar_jugador'),
    path('eliminar/<int:jugador_id>/', eliminar_jugador, name='eliminar_jugador'),
]
