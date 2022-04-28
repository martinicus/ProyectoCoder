from django.http import HttpResponse
import datetime

from django.template import Context, Template, loader


def saludo(request):
    return HttpResponse("Hola mundo!")

def segundaVista(request):
    return HttpResponse("<br><br><br><h2>Bien ya vamos entendiendo lo que son las vistas</h2>")

def diaDeHoy(request):
    dia=datetime.datetime.today()
    codigohtml="<h1>Hoy es: "+str(dia)+"</h1>"  
    return HttpResponse(codigohtml)

def saludoConNombre(self, nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calculaAñoNacimiento(self, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probandoHtml(self):
    nom="fran"
    ape="Di Martino"
    listaDeNotas=[1,5,6,8,4,3,9,8,7,4]
    diccionario={"nombre":nom,"apellido":ape, "lista":listaDeNotas}

    plantilla=loader.get_template("template1.html")
     
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

    



