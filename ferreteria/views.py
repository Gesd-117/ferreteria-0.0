from django.shortcuts import render
from typing import Dict, Any
# Create your views here.

def inicio(request):
    datos: Dict[str, Any] = {
        "titulo": "Página de inicio",
        "encabezado": "Ferreteria",
    }
    
    return render(request, 'ferreteria/index.html', datos)