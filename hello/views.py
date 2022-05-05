from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

global current_uid
current_uid = None

# Create your views here.
def index(request):
    user = "No input"
    date = "No input"
    if request.method == "POST":
        global current_uid
        user = request.POST.get('uid')
        current_uid = user
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
            global current_uid
            if request.POST.get('uid'):
                user = request.POST.get('uid')
                current_uid = user
            else:
                user = current_uid
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
            global current_uid
            if request.POST.get('uid'):
                user = request.POST.get('uid')
                current_uid = user
            else:
                user = current_uid
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