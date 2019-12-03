from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('You are in the index page')
    return render(request, 'main/base-template.html')
    # TODO: do something

# Create your views here.
