from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse(f"placeholder to later display a list of all the blogs")

def new(request):
    return HttpResponse(f"placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number} with a method named')

def destroy(request,number):
    return redirect('/')

def method(request):
    return JsonResponse({"foo": "fighters"})