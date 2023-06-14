from django.shortcuts import render

# Create your views here.

def home(request):
    content = "Welcome "
    return render(request, 'home/home.html', {'content':content})