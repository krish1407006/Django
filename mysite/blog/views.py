from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World! This is the home page of the blog app.")

# Create your views here.
