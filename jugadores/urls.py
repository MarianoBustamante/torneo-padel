from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importa la vista de logout

urlpatterns = [
    # Jugadores
    path('jugadores/', views.lista_jugadores, name='lista_jugadores'),
    path('jugadores/agregar/', views.agregar_jugador, name='agregar_jugador'),
    path('jugadores/editar/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('jugadores/eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    # Página de inicio
    path('', views.home, name='home'),
]
