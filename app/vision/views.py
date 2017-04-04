from django.shortcuts import render

# Create your views here.

def index(request):
    nombre = 'adrian'
    url = 'vision/index.html'
    context = {
        'nombre' : nombre
    }
    return render(request, url, context)