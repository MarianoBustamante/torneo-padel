from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador
from .forms import JugadorForm
from django.core.paginator import Paginator


def lista_jugadores(request):
    query = request.GET.get('q', '')  # Captura la búsqueda
    categoria_filtro = request.GET.get('categoria', '')  # Captura el filtro de categoría

    jugadores = Jugador.objects.all()
    if query:
        jugadores = jugadores.filter(nombre__icontains=query)  # Filtra por nombre
    if categoria_filtro:
        jugadores = jugadores.filter(categoria=categoria_filtro)  # Filtra por categoría

    categorias = dict(Jugador.CATEGORIAS)  # Lista de categorías disponibles

    # 🔹 PAGINACIÓN: Dividimos la lista en páginas de 10 jugadores
    paginator = Paginator(jugadores, 10)  # 10 jugadores por página
    page_number = request.GET.get('page')  # Obtenemos el número de página de la URL
    page_obj = paginator.get_page(page_number)  # Obtenemos la página correspondiente

    return render(request, 'jugadores/lista.html', {
        'page_obj': page_obj, 
        'categorias': categorias, 
        'query': query, 
        'categoria_filtro': categoria_filtro
    })



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