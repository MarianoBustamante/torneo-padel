from django.shortcuts import render, redirect
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
