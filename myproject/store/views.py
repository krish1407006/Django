from django.shortcuts import render

def home(request):
    return render(request, "store/home.html")

def home(request):
    context = {
        "name": "krish",



    }




# Create your views here.
