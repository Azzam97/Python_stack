from django.shortcuts import render, redirect
from .models import Course, Description
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)


def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request,value)
        return redirect('/')
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        Course.objects.create(name = name)
        Description.objects.create(desc = desc,
                                    course = Course.objects.get(name = name))
    return redirect('/')


def desc(request, id):
    context = {
        'course': Course.objects.get(id = id)
    }
    return render(request, "description.html", context)

def destroy(request, id):
    course = Course.objects.get(id = id)
    if 'No' in request.POST:
        return redirect('/')
    else:
        Course.delete(course)
        return redirect('/')
