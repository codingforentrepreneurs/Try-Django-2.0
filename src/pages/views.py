from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about_us_view(request):
    return render(request, "about.html", {})

def contact_us_view(request):
    return render(request, "contact.html", {})

def our_team_view(request):
    return HttpResponse("<h1>Team</h1>")