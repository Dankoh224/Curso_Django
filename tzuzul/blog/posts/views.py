from django.shortcuts import render

# Vamos a configurar nuestra función para devolver una respueta:
from django.http.response import HttpResponse

# Create your views here.

def post_list(request):
    return HttpResponse("Hola Mundo")