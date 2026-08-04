# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hello, World! This is the home page of the blog app.")

from django.shortcuts import render

from .models import Post

def home(request):

    posts = Post.objects.all()  # Fetch all posts from the database
    
    context = {
        "posts": posts,
   

    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")

# Create your views here.
