from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is the equivelent to @app.route('/')")

def greetings(requrst, name):
    return HttpResponse(f"hello {name}, how have you been? ")

def id_number(request, id, name):
    return HttpResponse(f"your id is {id} and your name is {name}")
