from django.shortcuts import render

# Create your views here.

def index(request):
    nombre = 'adrian'
    context = {
        'nombre' : nombre
    }
    return render(request, 'contacto/index.html', context)