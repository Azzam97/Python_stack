from django.shortcuts import render, redirect
from .models import Dojo, Ninja
# Create your views here.

def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)


def create_dojo(request):
    Dojo.objects.create(name = request.POST['name'],
                        city = request.POST['city'],
                        state = request.POST['state']
                        )
    return redirect('/')


def create_ninja(request):
    Ninja.objects.create(first_name = request.POST.get('first_name'),
                         last_name = request.POST['last_name'],
                         dojo = Dojo.objects.get(id=int(request.POST['dojo']))
                        )
    return redirect('/')


def delete_dojo(request, id):
    dojo = Dojo.objects.get(id = id)
    dojo.delete()
    return redirect('/')