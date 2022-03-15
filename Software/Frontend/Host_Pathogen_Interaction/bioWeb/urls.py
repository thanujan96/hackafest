"""Host_Pathogen_Interaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from distutils.command.upload import upload
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from bioWeb import views
urlpatterns = [
    path("",views.index,name="Index"),
    path("register/", views.register, name="Register"),
    path("login/", auth_views.LoginView.as_view(template_name='bioweb/login.html'), name="Login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='bioweb/indexnew.html'), name="Logout"),
    path("experiments/", views.collections, name="Collections"),
    path("colldelete/<id>", views.collDelete, name="CollDelete"),
    path("csvviews/<id>", views.csvView, name="CsvView"),
    path("csvdelete/<id>", views.csvDelete, name="CsvDelete"),
    path("readcsv/<id>", views.readCSV, name="ReadCSV"),
    path("sortcsv", views.sortcsv, name="SortCsv"),
    path("selectedrow/", views.selectedrow, name="selectedrow"),
    path("summa/", views.summa, name="summa"),
    path("visualizer/", views.visualizer, name="visualizer"),
    path("profile/", views.profile, name="Profile"),

]
