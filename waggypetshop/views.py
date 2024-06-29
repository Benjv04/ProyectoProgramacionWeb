from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    context={}
    return render(request,'waggypetshop/index.html',context)

def carrito(request):
    return render(request, 'waggypetshop/carrito.html')

def contacto(request):
    return render(request, 'waggypetshop/Contacto.html')

def gatos(request):
    return render(request, 'waggypetshop/gatos.html')

def inicioSesion(request):
    return render(request, 'waggypetshop/inicioSesion.html')

def nosotros(request):
    return render(request, 'waggypetshop/Nosotros.html')

def otros(request):
    return render(request, 'waggypetshop/otros.html')

def perros(request):
    return render(request, 'waggypetshop/perros.html')

def register(request):
    return render(request, 'waggypetshop/register.html')

def seguimiento(request):
    return render(request, 'waggypetshop/seguimiento.html')

def usuario_form(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = UsuarioForm()
    return render(request, 'waggypetshop/usuario_form.html', {'form': form})