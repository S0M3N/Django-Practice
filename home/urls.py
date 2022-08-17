from django.urls import path
from . import views

#urls for the apps here

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
]