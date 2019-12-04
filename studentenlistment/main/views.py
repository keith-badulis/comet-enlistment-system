from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from main.forms import ClassForm
from .models import Class, Profile


def index(request):
    classes_list = Class.objects.filter(students=request.user)
    context = {
        'classes_list': classes_list
    }
    return render(request, 'main/index.html', context)


def classes_view(request):
    classes_list = Class.objects.exclude(students=request.user)
    context = {
        'classes_list': classes_list
    }
    return render(request, 'main/classes-view.html', context)


def add_class(request, class_id):
    my_class = get_object_or_404(Class, pk=class_id)
    my_class.students.add(request.user)
    return HttpResponseRedirect(reverse('main:index'))





# def add_class(request):
#     if request.method == 'POST':
#         print('post')
#     else:
#         classes_list = Class.objects.exclude(students=request.user)
#         context = {
#             'classes_list': classes_list
#         }
#         return render(request, 'main/index.html', context)

