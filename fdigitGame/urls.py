from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name="add"),
    path('generate', views.generate, name="generate"),
    path('check', views.check, name="check")
]
