from django.shortcuts import render

def home(request):
    return render(request, "store/home.html")

def home(request):
    context = {
        "name": "krish",
        "course": "Django",
        "date": "2024-06-10",



    }
    return render(request, "store/home.html", context)




# Create your views here.
