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

def apiView(request):
    return render(request, "portfolio/tasks/api.html")

def calculatorView(request):
    return render(request, "portfolio/tasks/calculator.html")

def flexboxView(request):
    return render(request, "portfolio/tasks/flexbox.html")

def sqlView(request):
    return render(request, "portfolio/tasks/sql.html")

def websiteView(request):
    return render(request, "portfolio/tasks/website.html")

def flex_advView(request):
    return render(request, "portfolio/tasks/flex_adv.html")

def loginView(request):
    return render(request, "portfolio/tasks/login.html")