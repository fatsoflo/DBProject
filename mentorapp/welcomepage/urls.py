from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcomepage, name="welcomepage"),
]