# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hello, World! This is the home page of the blog app.")

from django.shortcuts import render

def home(request):
    context = {
        "name": "krish",
        "course": "Django",
        # "date": "2024-06-10",
        # "city": "hoshiarpur",
        # "college":"RBPU",
        # "is_student":False,
        # "age": 20,
        # "marks": 90
    }
    return render(request, "blog/home.html", context)

# Create your views here.
