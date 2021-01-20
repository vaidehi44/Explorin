from django.shortcuts import render
from django.http import HttpResponse

def homeView(request):
    return render(request, "portfolio/index.html")

def aboutView(request):
    return render(request, "portfolio/about.html")

def projectView(request):
    return render(request, "portfolio/project.html")

def contactView(request):
    return render(request, "portfolio/contact.html")
