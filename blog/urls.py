from django.urls import path
from . import views

#urls for the apps here

urlpatterns = [
    path('', views.blogIndex, name='blogindex'),
]