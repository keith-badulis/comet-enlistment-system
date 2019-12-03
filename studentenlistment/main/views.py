from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('You are in the index page')
    return render(request, 'main/index.html')
    # TODO: do something

# Create your views here.
