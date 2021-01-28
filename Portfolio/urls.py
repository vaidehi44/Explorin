from django.urls import path, include
from . import views


app_name = 'portfolio'

urlpatterns = [

    path('home',views.homeView, name='home'),
    path('about',views.aboutView, name='about'),
    path('projects',views.projectView, name='projects'),
    path('contact',views.contactView, name='contact'),
    path('tasks/api', views.apiView, name="api"),
    path('tasks/calculator', views.calculatorView, name="calculator"),
    path('tasks/flexbox', views.flexboxView, name="flexbox"),
    path('tasks/sql', views.sqlView, name="sql"),
    path('tasks/website', views.websiteView, name="website"),
    path('tasks/flexbox_advanced', views.flex_advView, name="flex_adv"),
    path('tasks/login_page', views.loginView, name="login_page"),


]

