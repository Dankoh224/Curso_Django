from django.shortcuts import render
from django.http.response import HttpResponse #No olvidar!!!
# Create your views here.
def post_list(request):
    return HttpResponse("Hola mundo, yo soy Vicente el ¡¡¡Dinosaurio!!!")