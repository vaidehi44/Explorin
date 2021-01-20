from django.urls import path, include
from . import views


app_name = 'portfolio'

urlpatterns = [

    path('home',views.homeView, name='home'),
    path('about',views.aboutView, name='about'),
    path('projects',views.projectView, name='projects'),
    path('contact',views.contactView, name='contact'),


]

