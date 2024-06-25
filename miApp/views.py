from django.shortcuts import render
from miApp.models import Estante, Producto

# Create your views here.
def index(request):
    estantes = Estante.objects.all()
    data = {'estantes' : estantes}
    return render(request, 'index.html', data)

def estante(request, e_id):
    productos = Producto.objects.filter(estante_id=e_id)
    estante = Estante.objects.get(id=e_id)
    data = {'productos' : productos, 'estante' : estante}
    return render(request, 'estante.html', data)

def create_estante(request):
    pass

def update_estante(request, e_id):
    pass

def delete_estante(request, e_id):
    pass

def create_producto(request):
    pass

def update_producto(request, p_id):
    pass

def delete_producto(request, p_id):
    pass
