from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerlist, name='customerlist'),
    path('customerlist/<int:cust_id>/', views.customerlist, name='customerlist'),

]