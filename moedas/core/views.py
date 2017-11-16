from django.shortcuts import render
from .models import Dolar

def home(request):
    #dolares = Dolar.objects.values().order_by('-data')[:1]
    dolares = Dolar.objects.values().order_by('-data')[0:1].get()
    return render(request, 'index.html', {'dolares':dolares})
