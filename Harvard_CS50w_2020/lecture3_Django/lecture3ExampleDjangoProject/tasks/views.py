from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#tasks = [] # global variable

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

    
# "tasks" above is a global variable, the entire app will have access to it
# have Django generate forms for you with LINES 1, 6, 22
    # in class NewTaskForm indentation, provide all of the fields of input you want the user to provide
    # CharField = character field = place for user to input characters/text
# Django forms more efficient than hard coding form by hand
    # make changes by editing one class form within views.py rather than having to edit several .html forms
# Priority = integer field, place where user can enter integers into form
    # min/max = constraints to ensure valid data, adds up/down arrows allowing you to select 1-10

# Ensuring input form data is valid
# Client side validation = web page encoded to know what acceptable values are for the form and will apply constraints on what user can enter into form/warning messages
# Server side validation is important because it's easy to disable client side validation/submit form bypassing client side validation, server version of page may be more upt to date than what a client sees in their web browser

# Create your views here.
def index(request):
    if "tasks" not in request.session: # "if I look inside the session (session = dictionary of all data on file about the user) then -next line"
        request.session["tasks"] = []    # then add the "tasks" variable (same as commented out above) and set it to an empty list []. creates empty task list for each individual user. Only works because "tasks" global list above LINE 6 is commented out (i.e. not in/does not exist in this session). "If the user does not already have a list of tasks, give them an empty list of tasks"
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] # corresponds to LINE 28, 29
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task] # for the current session's tasks list, add new task to the end of the list: tasks.   += is the same as .append
            return HttpResponseRedirect(reverse("tasks:index")) # redirect user to index page, reverse() function reverse engineers figuring out where the tasks:index page would be. import httpresponseredirect and reverse above
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()       # corresponds to form variable within add.html LINE 7
    })

# in Python, often will have Key and Value with a similar name, like "tasks": tasks
    # in "tasks": tasks, teh KEY to the left of the colon "tasks" is the name of the VARIABLE that you can access within the .html template with double curly braces via Django rendering
    # in "tasks": tasks, the VALUE to the right of the colon tasks is the VARIABLE in this .py file defined above on LINE 3
    # "Django has access to the Key on the left[for .html purposes] that contains the Value on the right[defined in Python code]" 

# LINE 34 add() gets called two different ways depending on request method
    # If you try to GET the add.html page, click on a link to the add.html page, go to the url in the address bar, then Django should just render a black form
    # if you POST data using POST request method, then you are submitting the form and a new task should be added to the tasks list
        # LINE 35: "if" statement checks for POST request method
            # "process the result of the request" => create a new variable: form, that will store user input
        # LINE 36: if you leave NewTaskForm()'s parameter blank it will generate a blank form
        # LINE 36: populate the NewTaskForm() with data: request.POST contains all of the data the user input when they submitted the form
        # LINE 37 and 39: form.cleaned_data = gives you access to all of the data the user input into the form (in this case, whatever the user submitted as a new "task"), you'll only get cleaned data if the form submits as valid/passes security check
        # LINE 38: save the cleaned data within a variable: task, so it can be accessed later, would not be viewable otherwise
        # LINE 39: tasks.append adds the user's task input to the list of tasks in views.py LINE 4
            # "if the form submits as valid, save the input into the variable 'task' and add variable task's value to the list of tasks"
        # Else statement: if the forum does not submit as valid, return the existing form data [keep the page the same with the user's input still in the form] so we can display to the user any errors that might have come up in the data they tried to submit 
        # need both client side and server side validation because if client side form is out of date it can fall back to the server for the most up to date version of web page

# simulate a different user accessing your page by opening incognito window in browser
# Django sessions allows different experience for each user (if list above is a global variable, anyone who accesses the web page will see the same exact list) 
# Django sessions remembers who you the user are and stores data based on your session with the web page (what you input into POST text fields, how you interacted with page)

# Django stores data inside tables, data about sessions in tables
    # if you get "no such table" error, run in terminal: python manage.py migrate
    # migrate creates all of the necessary default tables for Django to store data in its database

# Django remembers users' sessions using browser cookies