from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about_us_view(request):
    print(request.user)
    print(request.user.is_authenticated) # is_authenticated()
    the_username = request.user
    is_logged_in = request.user.is_authenticated
    context = {
        "username": the_username,
        "logged_in": is_logged_in
    }
    return render(request, "about.html", context)

def contact_us_view(request):
    return render(request, "contact.html", {})

def our_team_view(request):
    return HttpResponse("<h1>Team</h1>")