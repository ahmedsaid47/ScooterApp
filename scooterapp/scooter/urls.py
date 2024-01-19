from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("scooter", views.scooter, name="scooter_page"),
    path("scooter/<slug:slug>",views.scooter_details,name="scoot_details"),
    path("form", views.form, name="form"),
]