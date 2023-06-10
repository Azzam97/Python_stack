from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    if 'visits' not in request.session:
        request.session['visits'] = 1
        request.session['user'] = 1
    else:
        request.session['visits'] = request.session['visits'] + 1
        request.session['user'] = request.session['user'] + 1
    context = {
        'visits': request.session['visits'],
        'user': request.session['user']
    }
    return render(request, 'index.html', context)


def add_two(request):
    request.session['visits'] = request.session['visits'] + 2
    request.session['user'] = request.session['user'] + 1
    context = {
        'visits': request.session['visits'],
        'user': request.session['user']
    }
    return render(request, 'index.html', context)


def add_number(request):
    request.session['visits'] = request.session['visits'] + int(request.POST['number'])
    request.session['user'] = request.session['user'] + 1
    context = {
        'visits': request.session['visits'],
        'user': request.session['user']
    }
    return render(request, 'index.html', context)


def destroy_session(request):
    del request.session['visits']
    return redirect('/')