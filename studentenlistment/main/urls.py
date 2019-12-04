from django.conf.urls import url
from django.urls import path

from main import views

app_name = 'main'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('class/', views.list_class, name='list-class'),
    path('class/<int:class_id>/add', views.add_class, name='add-class'),
    path('class/<int:class_id>/delete', views.delete_class, name='delete-class'),
]