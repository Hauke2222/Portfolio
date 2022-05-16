from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("posts/<int:pk>/", views.detail, name="post_detail"),
]
