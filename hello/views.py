from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

from .models import Greeting

# Create your views here.
def index(request):
    user = "No input"
    date = "No input"
       
    return render(request, "base.html", {
        "venues": ["dllm", "on99"],
        "subject": user,
        "date": date,
    })

def venues(request):
    if request.method == "POST":
        user = request.POST.get('uid')
        date = request.POST.get('date')
        request.session['uid'] = user
        request.session['date'] = date
        #api call
        url1 = "https://thawing-island-30523.herokuapp.com/backend/api/venues?uid="+str(user)+"&date="+str(date)  
        response1 = requests.get(url1)
        print(response1.text)
        result1 = response1.json()
        return render(request, "venues.html", {
            "venues": result1['Venues'],
            "subject": user,
            "date": date,
        })
    else:
        request.session['uid'] = "No input"
        request.session['date'] = "No input"
        user = request.session['uid']
        date = request.session['date']
        return render(request, "venues.html", {
            "venues": ["No Data"],
            "subject": user,
            "date": date,
        })


def contacts(request):
    if request.method == "POST":
        user = request.POST.get('uid')
        date = request.POST.get('date')
        request.session['uid'] = user
        request.session['date'] = date
        #api call
        url2 = "https://thawing-island-30523.herokuapp.com/backend/api/contacts?uid="+str(user)+"&date="+str(date)  
        response2 = requests.get(url2)
        print(response2.text)
        result2 = response2.json()
        return render(request, "contacts.html", {
            "venues": result2['UID'],
            "subject": user,
            "date": date,
        })
    else:
        request.session['uid'] = "No input"
        request.session['date'] = "No input"
        user = request.session['uid']
        date = request.session['date']
        return render(request, "contacts.html", {
            "venues": ["No Data"],
            "subject": user,
            "date": date,
        })
