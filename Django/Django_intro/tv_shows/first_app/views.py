from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)


def show_info(request, id):
    context = {
        'show': Show.objects.get(id = id)
    }
    return render(request, 'show_info.html', context)


def edit(request,id):
    context = {
        'show': Show.objects.get(id = id)
    }
    return render(request, "edit_show.html", context)


def go_to(request, id):
    show = Show.objects.get(id = id)
    return redirect(f'shows/{show.id}')


def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
    return redirect(f'/shows/{id}')


def destroy(request, id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect('/shows')


def new(request):
    return render(request, "new_show.html",)


def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/shows/new')
    else:
        show = Show.objects.create(title = request.POST.get('title'),
                               network = request.POST.get('network'),
                               release_date = request.POST.get('release_date'),
                               desc = request.POST.get('desc')
                        )
    return redirect(f'/shows/{show.id}')
