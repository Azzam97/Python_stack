from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    request.session['number'] = random.randint(1,100)
    request.session['attempts'] = 0
    return render(request, 'index.html')


def process(request):
    request.session['attempts'] = request.session['attempts'] + 1
    if int(request.POST['number']) > request.session['number']:
        text = 'Too High'
        color = 'red'
    elif int(request.POST['number']) < request.session['number']:
        text = 'Too Low'
        color = 'red'
    else:
        text = f"{request.POST['number']} was the number!"
        color = 'green'
    if request.session['attempts'] == 5:
        text = "You Lose"
        color = 'red'
        context = {
            'text': text,
            'color': color,
            'attempts': request.session['attempts']
        }
        return render(request,"lose.html", context)
    context = {
        'text': text,
        'color': color,
        'attempts': request.session['attempts']
    }
    return render(request, 'index.html', context)


def destroy_session(request):
    del request.session['number']
    del request.session['attempts']
    return redirect('/')
