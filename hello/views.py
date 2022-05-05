from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, "base.html", {
        "venues": ["this subject", "on99"],
        "subject": "3025704501",
        "date": "2022-05-05",
    })

def venues(request):
    return render(request, "venues.html", {
        "venues": ["dllm", "on99"],
        "subject": "3025704501",
        "date": "2022-05-05",
    })

def contacts(request):
    return render(request, "contacts.html", {
        "venues": ["dllm", "on99"],
        "subject": "3025704501",
        "date": "2022-05-05",
    })