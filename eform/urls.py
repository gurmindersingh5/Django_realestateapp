from django.urls import path
from . import views

urlpatterns = [
    path('', views.e_form, name='e_form')
]