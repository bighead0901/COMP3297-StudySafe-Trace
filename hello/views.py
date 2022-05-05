from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

from .models import Greeting

# Create your views here.
def index(request):
    user = "No input"
    date = "No input"
    if request.method == "POST":
        user = request.POST.get('uid')
        date = request.POST.get('date')
        request.session['uid'] = user
        request.session['date'] = date
    else:
        request.session['uid'] = "No input"
        request.session['date'] = "No input"
        
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
            #api call
            url1 = "https://comp3297groupproject.herokuapp.com/backend/api/venues?uid="+str(user)+"&date="+str(date)  
            response1 = requests.get(url1)
            print(response1.text)
            result1 = response1.json()
            return render(request, "venues.html", {
                "venues": result1['Venues'],
                "subject": user,
                "date": date,
            })

def contacts(request):
    if request.method == "POST":
        if request.POST.get('contacts'):
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