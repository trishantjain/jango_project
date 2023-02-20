from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

def blogs(request):
    myPosts = Blogpost.objects.all()
    return render(request, "blog/blogs.html", {'myposts': myPosts})

def blogContent(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, "blog/blog_content.html", {"post": post})
