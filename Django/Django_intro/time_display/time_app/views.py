from django.shortcuts import render
from time import strftime, localtime
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'time': strftime("%Y-%m-%d %H:%M %p", localtime()),
        'time2': datetime.now()
    }
    return render(request, "index.html", context)
