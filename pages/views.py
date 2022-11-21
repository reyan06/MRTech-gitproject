from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')
    

def about(request):
    return render(request, 'pages/about.html')


def computer(request):
    return render(request, 'pages/computer.html')


def laptop(request):
    return render(request, 'pages/laptop.html')


def product(request):
    return render(request, 'pages/product.html')

def contact(request):
    return render(request, 'pages/contact.html')
