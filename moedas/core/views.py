from django.shortcuts import render
from .models import Dolar
import json


def retponto(valor):
    return valor.replace(",",".")


def transfloat(lista):
    """Transforma lista de string para float"""
    listafloat = []
    for x in lista:
        svirg = retponto(x)
        numfl = float(svirg)
        listafloat.append(numfl)
    return listafloat


def home(request):
    #dolares = Dolar.objects.values().order_by('-data')[:1]
    dolares = Dolar.objects.values().order_by('-id')[0:1].get()
    queryset = Dolar.objects.all()
    data = [obj.data for obj in queryset]
    #dolar = [int(obj.venda) for obj in queryset]
    dolar = [obj.venda for obj in queryset]
    dolarconv = transfloat(dolar)

    context = {
        'data': json.dumps(data),
        'dolar': json.dumps(dolarconv),
    }

    return render(request, 'index.html', {'dolares':dolares, 'context':context})


