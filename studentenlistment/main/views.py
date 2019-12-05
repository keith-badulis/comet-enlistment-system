from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from main.forms import ClassForm
from .models import Class, Profile, User, College

from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    classes_list = Class.objects.filter(students=request.user)
    context = {
        'classes_list': classes_list
    }
    return render(request, 'main/index.html', context)


@login_required
def list_available_classes(request):
    classes_list = Class.objects.exclude(students=request.user)
    context = {
        'classes_list': classes_list
    }
    return render(request, 'main/available-classes-view.html', context)


@login_required
def add_class(request, class_id):
    my_class = get_object_or_404(Class, pk=class_id)
    # student = User.objects.get(username=request.user.username)
    # for c in student.class_set:
    #     if c.
    my_class.students.add(request.user)
    return HttpResponseRedirect(reverse('main:index'))


@login_required
def delete_class(request, class_id):
    my_class = get_object_or_404(Class, pk=class_id)
    my_class.students.remove(request.user)
    return HttpResponseRedirect(reverse('main:index'))


def logout_page(request):
    logout(request)
    return redirect('/')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Input a valid DLSU email address.', required=True)
    id_number = forms.CharField(max_length=8, required=True)
    college = forms.ModelChoiceField(queryset=College.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'id_number', 'college', 'password1', 'password2', )

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        if domain != 'dlsu.edu.ph':
            raise forms.ValidationError("Please use your DLSU email")
        return data


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.id_number = form.cleaned_data.get('id_number')
            user.profile.college = form.cleaned_data.get('college')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('main:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
