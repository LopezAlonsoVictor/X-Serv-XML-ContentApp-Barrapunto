from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages
from .models import Titular
from .xmlparserbarrapunto import getrss

FORMULARIO = '''
            <form action="" Method="POST">
            Introduce:<br>
            <input type="text" name="name" placeholder="name">
            <input type="text" name="page" placeholder="page"><br>
            <input type="submit" value="Enviar">
</form>
'''
   

@csrf_exempt
def barra(request):
    if request.method == "POST":
        nuevo = Pages(name=request.POST['name'],page=request.POST['page'])
        nuevo.save()
    lista = Pages.objects.all()
    respuesta = '<ul>'
    for page in lista:
        respuesta += '<li>' + page.name
    respuesta += "</ul>"
    respuesta += FORMULARIO
    respuesta += Titular.objects.get(name="barrapunto").html
    return HttpResponse(respuesta)

def page(request, nombre):
    try:
        page = Pages.objects.get(name=nombre)
    except Pages.DoesNotExist:
        raise Http404("No existe")
    return HttpResponse(page.page)

def update(request):
    Titular.objects.all().delete()
    titular = Titular(name="barrapunto",html=getrss())
    titular.save()
    return HttpResponse("Barrapunto actualizada<br><br>"+str(Titular.objects.get(name="barrapunto").html))
    
