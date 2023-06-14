from django.urls import path
from . import views

urlpatterns = [
    path('', views.c_form, name='c_form')
]