# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'fixedPages/home.html')

def contact(request):
    return render(request, 'fixedPages/contact.html')