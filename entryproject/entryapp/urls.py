from django.contrib import admin
from django.urls import path, include
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello'),
]