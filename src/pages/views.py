from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about_us_view(request):
    return render(request, "about.html", {})

def contact_us_view(some_arg):
    return HttpResponse("<h1>Contact</h1>")

def our_team_view(some_arg):
    return HttpResponse("<h1>Team</h1>")