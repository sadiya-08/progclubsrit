from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("compt", views.compt, name='compt'),
    path("resources", views.resources, name='resources'),
    path("testimonals", views.testimonals, name='testimonals'),
    path("blog", views.blog, name='blog'),
    

    
]
