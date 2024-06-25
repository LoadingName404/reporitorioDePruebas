from django.shortcuts import render, redirect
from django.contrib import messages
from miApp.models import Estante, Producto
from miApp.form import FormEstante, FormProducto

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

def create_estante(req):
    form = FormEstante()

    if req.method == "POST":
        try:
            form = FormEstante(req.POST)
            if form.is_valid():
                form.save()
                estante = Estante.objects.last()
                messages.success(req, f'Se agrego el estante {estante.numero} correctamente.')
                return redirect('/')
        except Exception as e:
            messages.error(req, f'No se pudo agregar el estante. Error: {str(e)}')

    data = {'form': form, 'accion': 'Agregar', 'descripcion': 'Agregue el numero del estante nuevo que desea agregar.'}
    return render(req, 'cu_estante.html', data)


def update_estante(request, e_id):
    pass

def delete_estante(req, e_id):
    estante = Estante.objects.get(id=e_id)
    try:
        estante.delete()
        messages.success(req, f'Se elimino el estante {estante.numero} correctamente.')
    except Exception as e:
        messages.error(req, f'No se pudo eliminar el estante. Error: {str(e)}')
    return redirect('/')

def create_producto(req, e_id):
    form = FormProducto()

    if req.method == "POST":
        try:
            form = FormProducto(req.POST)
            print(form)
            if form.is_valid():
                form.save()
                producto = Producto.objects.last()
                messages.success(req, f'Se agrego el producto {producto.nombre} correctamente.')
                return redirect('/')
        except Exception as e:
            messages.error(req, f'No se pudo agregar el producto. Error: {str(e)}')

    data = {'form': form, 'accion': 'Agregar', 'descripcion': 'Agregue el numero del estante nuevo que desea agregar.'}
    return render(req, 'cu_producto.html', data)

def update_producto(request, p_id):
    pass

def delete_producto(request, p_id):
    pass
