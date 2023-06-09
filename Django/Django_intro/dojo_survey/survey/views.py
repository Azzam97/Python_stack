from django.shortcuts import render, redirect

# Create your views here.

def form(request):
    return render(request, 'index.html')


def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    context = {
        'name': name,
        'location': location,
        'language': language,
        'comment': comment,
        'gender': gender,
        'hobby': hobby,
    }
    return render(request, 'result.html', context)


def go_back(request):
    return redirect('/')

