from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    user = "No input"
    date = "No input"
    if request.method == "POST":
        user = request.POST.get('uid')
        date = request.POST.get('date')
        request.session['uid'] = user
        request.session['uid'] = date
    else:
        request.session['uid'] = "No input"
        
    return render(request, "base.html", {
        "venues": ["dllm", "on99"],
        "subject": user,
        "date": date,
    })

def venues(request):
    if request.method == "POST":
        if request.POST.get('venues'):
            if request.POST.get('uid'):
                user = request.POST.get('uid')
            else:
                user = request.session['uid']
            if request.POST.get('date'):
                date = request.POST.get('date')
            else:
                date = request.session['date']
            return render(request, "venues.html", {
                "venues": ["dllm", "on99"],
                "subject": user,
                "date": date,
            })

def contacts(request):
    if request.method == "POST":
        if request.POST.get('contacts'):
            global current_uid
            if request.POST.get('uid'):
                user = request.POST.get('uid')
            else:
                user = request.session['uid']
            if request.POST.get('date'):
                date = request.POST.get('date')
            else:
                date = request.session['date']
            return render(request, "contacts.html", {
                "venues": ["dllm", "on99"],
                "subject": user,
                "date": date,
            })