from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def message(request):
    return HttpResponse("my message!")

def index(request):
    mydict = {'insert_me': "Hello I am from views.py!"}
    # return render(request, 'index.html', context=mydict)
    return render(request, 'index.html')