from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('computer', views.computer, name='computer'),
    path('laptop', views.laptop, name='laptop'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),


]
