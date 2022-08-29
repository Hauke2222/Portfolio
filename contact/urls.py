from django.urls import path

from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("submit", views.submit, name="submit"),
]
