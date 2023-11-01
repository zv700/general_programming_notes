from django.contrib.auth import authenticate, login, logout # authenticate checks to see if user's username and password are correct
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request): # index function needs to display info about the currently signed-in user after they login to the page
    if not request.user.is_authenticated:    # "What should happen when someone tries to access this page when they are not authenticated?" --- request object that gets passed in as part of the request to every user in Django automatically has a user associated with it --- is_authenticated tells whether a user is signed in or not
        return HttpResponseRedirect(reverse("login"))   # "if a user is not authenticated/logged in we are going to redirect them to the login view"
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)  # authenticate() function takes a request, a username(stored in variable: username), a password (stored in variabe: password) --> if authenticate check passes, authenticate() gives back who the user actually is 
        if user is not None:    # as long as user is not none, that means the user was authenticated sucessfully --> logs the user in using login() function --> httpredirect user back to the index path
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:                                               # else: return invalid credentials message --> in login.html use if logic to display message in a div
            return render(request, "users/login.html", {
                "message": "Invalid Credentials."
            })
        
    return render(request, "users/login.html") # render a form on an html template where the user can log themself in

def logout_view(request):
    return render(request, "users/login.html", {
        "message": "Logged out."
    })