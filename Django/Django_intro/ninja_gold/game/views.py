from django.shortcuts import render,redirect
from datetime import datetime
import random

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['text'] = []
        request.session['amount'] = 0
        request.session['color'] = ''
    context = {
        'gold': request.session['gold'],
        'text': request.session['text'],
        'amount': request.session['amount'],
        'color': request.session['color']
    }
    return render(request, 'index.html', context)

def process_money(request):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
    if request.POST['building'] == 'farm':
        amount = random.randint(10,20)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a Farm and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif request.POST['building'] == 'cave':
        amount = random.randint(5,10)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a Farm and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif request.POST['building'] == 'house':
        amount = random.randint(2,5)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a Farm and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif request.POST['building'] == 'quest':
        amount = random.randint(-50,50)
        if amount > 0:
            request.session['amount'] = amount
            request.session['gold'] += amount
            text = f"You entered a Farm and earned {amount} gold. {timestamp}"
            color = 'green'
            request.session['color'] = color
        elif amount < 0:
            request.session['amount'] = amount
            request.session['gold'] += amount
            text = f"You Failed a quest and lost {amount} gold. Ouch. {timestamp}"
            color = 'red'
            request.session['color'] = color
    request.session['text'].insert(0,text)
    return redirect('/')


def reset(request):
    del request.session['gold']
    return redirect('/')


def manual(request, name):
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
    if name == 'farm':
        amount = random.randint(10,20)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a Farm and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif name == 'cave':
        amount = random.randint(5,10)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a cave and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif name == 'house':
        amount = random.randint(2,5)
        request.session['amount'] = amount
        request.session['gold'] += amount
        text = f"You entered a house and earned {amount} gold. {timestamp}"
        color = 'green'
        request.session['color'] = color
    elif name == 'quest':
        amount = random.randint(-50,50)
        if amount > 0:
            request.session['amount'] = amount
            request.session['gold'] += amount
            text = f"You entered a quest and earned {amount} gold. {timestamp}"
            color = 'green'
            request.session['color'] = color
        elif amount < 0:
            request.session['amount'] = amount
            request.session['gold'] += amount
            text = f"You Failed a quest and lost {amount} gold. Ouch. {timestamp}"
            color = 'red'
            request.session['color'] = color
    request.session['text'].insert(0,text)
    return redirect('/')
