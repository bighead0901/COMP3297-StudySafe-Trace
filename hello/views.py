from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    user = "No input"
    date = "No input"
    if request.method == "POST":
        user = request.POST.get('uid')
        if user == "3025704501":
            date = "2022-05-05"
        else:
            date = "No record"
        
    return render(request, "base.html", {
        "venues": ["dllm", "on99"],
        "subject": user,
        "date": date,
    })

def venues(request):
    if request.method == "POST":
        if request.POST.get('venues'):
            user = request.POST.get('uid')
            if user == "3025704501":
                date = "2022-05-05"
            else:
                date = "No record"
            return render(request, "venues.html", {
                "venues": ["dllm", "on99"],
                "subject": user,
                "date": date,
            })
        else:
            return render(request, "base.html", {
                "subject": "No input",
                "date": "No input",
            })

def contacts(request):
    if request.method == "POST":
        if request.POST.get('contacts'):
            user = request.POST.get('uid')
            if user == "3025704501":
                date = "2022-05-05"
            else:
                date = "No record"
            return render(request, "contacts.html", {
                "venues": ["dllm", "on99"],
                "subject": user,
                "date": date,
            })
        else:
            return render(request, "base.html", {
                "subject": "No input",
                "date": "No input",
            })