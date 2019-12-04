from django.conf.urls import url
from django.urls import path

from main import views

app_name = 'main'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('classes/', views.classes_view, name='classes-view'),
    path('class/<int:class_id>/add', views.add_class, name='add-class'),
]