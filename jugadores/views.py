from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import JugadorForm, CustomAuthenticationForm
from .models import Jugador
from .forms import CustomUserCreationForm
from collections import Counter
from django.db.models import Count, Avg
# Vista de agregar jugador
@login_required
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')  # Redirige a la lista de jugadores
    else:
        form = JugadorForm()

    return render(request, 'jugadores/agregar.html', {'form': form})

# Vista de lista de jugadores con búsqueda y filtrado por categoría
def lista_jugadores(request):
    query = request.GET.get("q", "")
    categoria_filtro = request.GET.get("categoria", "")

    jugadores = Jugador.objects.all()

    # Filtrar por nombre (si se ha pasado un término de búsqueda)
    if query:
        jugadores = jugadores.filter(nombre__icontains=query)

    # Filtrar por categoría (si se ha pasado un filtro de categoría)
    if categoria_filtro:
        jugadores = jugadores.filter(categoria=categoria_filtro)

    # Obtener estadísticas por categoría
    estadisticas = jugadores.values("categoria").annotate(total=Count("id"))

    # Diccionario de categorías para la selección en el filtro
    CATEGORIAS = {
        "1ra": "Primera",
        "2da": "Segunda",
        "3ra": "Tercera",
        "4ta": "Cuarta",
        "5ta": "Quinta",
        "6ta": "Sexta",
        "7ma": "Séptima",
        "8va": "Octava",
    }

    # Para la paginación
    paginator = Paginator(jugadores, 10)  # Muestra 10 jugadores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Estadísticas
    categoria_max_jugadores = estadisticas.order_by('-total').first()
    categorias_data = [estadistica['total'] for estadistica in estadisticas]
    categorias_labels = [CATEGORIAS.get(estadistica['categoria'], estadistica['categoria']) for estadistica in estadisticas]

    # Calcular promedio de edad
    promedio_edad = jugadores.aggregate(promedio=Avg('edad'))['promedio'] or 0

    context = {
        "jugadores": jugadores,
        "query": query,
        "categoria_filtro": categoria_filtro,
        "categorias": CATEGORIAS,
        "estadisticas": estadisticas,
        "categoria_max_jugadores": categoria_max_jugadores,
        "categorias_data": categorias_data,
        "categorias_labels": categorias_labels,
        "promedio_edad": promedio_edad,
        "page_obj": page_obj,
    }

    return render(request, "jugadores/lista.html", context)



# Vista de editar jugador
@login_required
def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)

    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')
    else:
        form = JugadorForm(instance=jugador)

    return render(request, 'jugadores/editar.html', {'form': form, 'jugador': jugador})

# Vista de eliminar jugador
@login_required
def eliminar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)

    if request.method == 'POST':
        jugador.delete()
        return redirect('lista_jugadores')

    return render(request, 'jugadores/eliminar.html', {'jugador': jugador})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()

    # Código asegurado que siempre se ejecuta
    return render(request, 'jugadores/login.html', {'form': form})
# Vista de registro
def registro_view(request):
    if request.user.is_authenticated:
        return redirect('lista_jugadores')  # Redirige si ya está logueado

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()

    return render(request, 'jugadores/registro.html', {'form': form})

# Vista de inicio (home)
def home(request):
    return render(request, 'jugadores/home.html')

def logout_view(request):
    logout(request)
    return redirect('home') 
