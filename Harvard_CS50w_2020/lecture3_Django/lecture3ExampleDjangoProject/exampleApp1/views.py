from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# "Each view is something the user might want to see."
# Create a Django view by defining a function

#def index(request): # request = HTTP request the user makes to access the page/web server, contains accessable data
#    return HttpResponse("Hello! This is the index page.") # HttpResponse = a special class created by Django, must be imported to be able to use in code, instructions in Django documentation

def index(request):
    return render(request, "exampleApp1/index.html") # render takes two arguments: a request and an html template. write the directory path to the .html file within the templates folder ==> templates/exampleApp1/index.html - you can leave out "templates" directory

# functon index() returns "Hello, world!" in response to a user's web browser's request to access the web server/web page
# What url is the user/client trying to access?
# must tell the app when to return the response in urls.py either in project folder (urls.py that controls entire project) or a urls.py specific for each app

def pageone(request):
    return HttpResponse("Welcome to page one!")

def pagetwo(request):
    return HttpResponse("Welcome to page two!")

#def greet(request, name):
#    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "exampleApp1/greet.html", {
        "name": name.capitalize()
    })

# greet() function overwrites pageone() and pagetwo() because they all accomplish the same thing: greeting the user, but greet() has a wider scope of functionality: greeting any name, whereas pageone and pagetwo are specific to those inputs
# .capitalize() following a string will capitalize the first letter, in greet() name.capitalize will capitalize the name entered as a string in the url into the fstring

# an HttpResponse() can be any HTML content: lists, tables, etc.
    # write the html template/.html file and link it to a page using the return function (see above: LINE 13)
    # LINE 13: prefix your .html templates with a directory name to "namespace" them: index.html is within its own folder "exampleApp1" to "name the space" because there might be multiple different "index.html" files throughout one Django project that must each be named "index.html" but are their own unique page. "Editing this specific index.html file located within the 'exampleApp1' folder"

# render() function's 3rd argument: context ==> in curly braces
    # context = all of the information you want to provide to the .html template, example: all of the variables you want the template to have access to
    # context parameter is a Python dictionary {Key:Value}
    # LINE 30: giving the template access to a variable/KEY called "name". The KEY's VALUE is equal to name.captialize() where this input name comes from the name argument within function greet(request, name) from LINE 28