from typing import Any
from django.urls import path
from . import views
urlpatterns: list[Any] = [
    path('', views.home, name='home'),
    path('products/<slug>/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('single/<int:pk>/', views.single, name='single'),
    path('register/', views.register, name='register'),]