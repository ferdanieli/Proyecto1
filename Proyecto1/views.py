import datetime

from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo2(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaHoy(request):
    dia = datetime.datetime.now()
    documentodetexto = f"Hoy es: <br> {dia}"
    return HttpResponse(documentodetexto)

def miNombreEs(self, nombre):
    documentodetexto = f"Mi nombre es: <br> {nombre}"
    return HttpResponse(documentodetexto)

# def probandoTemplate(request):
    nombre = "Fer"
    edad = 45
    dia = datetime.datetime.now()
    notas= [2,2,3,7,2,5]
    contexto = {"nombre": nombre, "edad": edad, "dia": dia, "notas": notas}
    return render(request, "templates1.html", contexto)

# estoy probando git