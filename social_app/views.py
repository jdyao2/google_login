from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, "social_app/index.html")

def about(request):
    return render(request, "social_app/about.html")

def contact(request):
    return render(request, "social_app/contact.html")


def logout(request):
    return render(request, "social_app/logout.html")
