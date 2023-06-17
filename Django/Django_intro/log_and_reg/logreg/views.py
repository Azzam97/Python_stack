from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def index(request):
    return render(request, "index.html")


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        request.session['username'] = fname + " " + lname
        request.session['status'] = "Registered"
        User.objects.create(first_name = fname,
                        last_name = lname,
                        email = email,
                        password = pw_hash
                        )
        return redirect('/success')


def success(request):
    if 'username' not in request.session:
        return redirect('/')
    context = {
        'username': request.session['username'],
        'status': request.session['status']
    }
    return render(request, "success.html", context)


def login(request):
    errors2 = User.objects.login_validator(request.POST)
    if len(errors2) > 0:
        for value in errors2.values():
            messages.error(request, value)
        return redirect('/')
    else:
        email2 = request.POST['email2']
        user = User.objects.filter(email = email2)
        request.session['username'] = user[0].first_name + " " + user[0].last_name
        request.session['status'] = "Logged in"
        return redirect('/success')


def logout(request):
    request.session.flush()
    return redirect('/')
