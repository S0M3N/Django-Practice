from django.urls import path
from . import views

#urls for the apps here

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
]