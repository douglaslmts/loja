from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

def home_app(request):
    return HttpResponse("Pagina de inicio Aplicativo")
