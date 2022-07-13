from django.shortcuts import render
#Importo el modelo para poder crear los objetos
from app_imc.models import Persona


def index(request):
    
    if request.GET:
        nombre = request.GET.get("nombre")
        altura = request.GET.get("altura")
        peso = request.GET.get("peso")
        #En base al modelo, creo un objeto que voy a estar almacenando en la base
        persona = Persona(nombre = nombre, imc_calculado = 0)
        persona.calcular_imc(float(altura), float(peso))
        persona.save()
        
        return render(request, "app_imc/index.html", {"persona": persona})
        
    
    return render(request, "app_imc/index.html", {})
