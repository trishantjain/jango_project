from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogs, name="BlogHome"),
    path("blogcont/<int:id>", views.blogContent, name="Blogpost")
]