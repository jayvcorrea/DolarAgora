from django.shortcuts import render
import os

# Create your views here.
def dolar_agora(request):
    return render(request, 'core/dolar_agora.html')

def home(request):
    return render(request, 'core/index.html')
