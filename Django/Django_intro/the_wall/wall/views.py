from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

# Create your views here.

def index(request):
    return render(request, "logreg.html")


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
        request.session['status'] = "You have registered successfully"
        request.session['lname'] = lname
        request.session['fname'] = fname
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
        'status': request.session['status'],
        'messages': Message.objects.all().order_by('-created_at')
    }
    return render(request, "wall.html", context)


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
        request.session['fname'] = user[0].first_name
        request.session['lname'] = user[0].last_name
        request.session['status'] = "Logged in"
        return redirect('/success')
    

def create_message(request):
    first_name = request.session['fname']
    Message.objects.create(message = request.POST['message'],
                           user = User.objects.get(first_name = first_name)
                           )
    return redirect('/success')


def create_comment(request, id):
    first_name = request.session['fname']
    Comment.objects.create(comment = request.POST['comment'],
                           comment_user = User.objects.get(first_name = first_name),
                           comment_message = Message.objects.get(id = id)
                           )
    return redirect('/success')


def delete(request, id):
    message = Message.objects.get(id = id)
    Message.delete(message)
    return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')
