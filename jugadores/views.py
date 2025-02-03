from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador
from .forms import JugadorForm

def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores/lista.html', {'jugadores': jugadores})

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')
    else:
        form = JugadorForm()
    
    return render(request, 'jugadores/agregar.html', {'form': form})

def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')  # Asegúrate de que la URL es correcta
    else:
        form = JugadorForm(instance=jugador)
    
    return render(request, 'jugadores/editar.html', {'form': form, 'jugador': jugador})

def eliminar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('lista_jugadores')
    
    return render(request, 'jugadores/eliminar.html', {'jugador': jugador})