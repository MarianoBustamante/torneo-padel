from django.urls import path
from .views import lista_jugadores, agregar_jugador, editar_jugador, eliminar_jugador,home_view, registro_view,login_view
from . import views

urlpatterns = [
    path('', lista_jugadores, name='lista_jugadores'),
    path('agregar/', agregar_jugador, name='agregar_jugador'),
    path('editar/<int:jugador_id>/', editar_jugador, name='editar_jugador'),
    path('eliminar/<int:jugador_id>/', eliminar_jugador, name='eliminar_jugador'),
    path('registro/', views.registro_view, name='registro'),
    path('', views.home_view, name='home'),
    path('', views.home_view, name='home'),  # Página de inicio
    path('registro/', views.registro_view, name='registro'),  # Registro de usuario
    path('login/', views.login_view, name='login'),  # Login de usuario
     path('', views.home_view, name='home'),  # Esta es la página de inicio
    path('registro/', views.registro_view, name='registro'),  # Ruta para el registro
]
