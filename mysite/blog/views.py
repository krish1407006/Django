# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hello, World! This is the home page of the blog app.")

from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html")

# Create your views here.
