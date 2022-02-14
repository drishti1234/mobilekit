from django.shortcuts import render

# Create your views here.

def appPage(request):
    return render(request, 'mobilekit/app-pages.html')

def appComponent(request):
    return render(request, 'mobilekit/app-components.html')

def accordion(request):
    return render(request, 'mobilekit/component-accordion.html')

def index(request):
    return render(request, 'mobilekit/index.html')

def cart(request):
    return render(request, 'mobilekit/page-cart.html')

def chat(request):
    return render(request, 'mobilekit/page-chat.html')