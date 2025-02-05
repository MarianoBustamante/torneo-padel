from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import JugadorForm, CustomAuthenticationForm
from .models import Jugador
from .forms import CustomUserCreationForm
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
    query = request.GET.get('q', '')
    categoria_filtro = request.GET.get('categoria', '')

    jugadores = Jugador.objects.all()

    if query:
        jugadores = jugadores.filter(nombre__icontains=query)

    if categoria_filtro:
        jugadores = jugadores.filter(categoria=categoria_filtro)

    paginator = Paginator(jugadores, 10)  # 10 jugadores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Jugador.CATEGORIAS  # para el filtro de categorías

    return render(request, 'jugadores/lista.html', {
        'page_obj': page_obj,
        'query': query,
        'categoria_filtro': categoria_filtro,
        'categorias': categorias
    })

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
