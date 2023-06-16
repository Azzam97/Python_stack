from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Blog

# Create your views here.
def index(request):
    return render(request, "index.html")

def update(request):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    else:
        Blog.objects.create(name = request.POST['name'],
                            desc = request.POST['desc']
        )
        messages.success(request, "Blog successfully updated")
        return redirect('/')
