from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("", views.crop_recommendation, name="crop_recommendation"),
]
