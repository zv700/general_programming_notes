# variable: urlpatterns is a list of all allowable urls that are accessable for this specific app
# import "path" from "django.urls" to be able to create urls
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pageone", views.pageone, name="pageone"),
    path("pagetwo", views.pagetwo, name="pagetwo"),
    path("<str:name>", views.greet, name="greet")
]

# 1rst path() argument [LINE 8] = when someone visits default url run the index function(view), just double quotes "" is an empty string = no additional argument/nothing at the end of the route, empty url
# 1rst path() argument [IN GENERAL] = determines the directory associated with this view within the url [examplewebpage.com/exampleappname/firstpathargument/]
# 2nd path() argument = what view should be rendered when this url is visited ==> views.index = index function from views.py in same folder; fileName.functionName
# 3rd path() argument [optional] = string name to identify this specific url, giving a name to a specific urlpattern makes it easy to reference that url from other parts of the application (example: when you are making links betwee pages, forums submitting to different parts of web app)

# "from ." = from the current directory (same folder in the file structure), single dot on its own .  
# any time you use a variable name from another file (like views.py), you need to import that file into the current page's code (from . import views <== imports views.py from current directory because urls.py and views.py are located in the same folder)

# after creating a urls.py for a specific application, go to the main urls.py located in the Django project folder, add a path to the Django app's urls.py in the list "urlpatterns" inside of the urls.py in the Django PROJECT folder

# path("<str:name>") , can replace "name" with anything, means the specified string that is the second parameter of greet() function in views.py will be a string that will be the user's name
# path("<str:name>") takes any string placed in the "name" parameter of greet() function in views.py
# when a user accesses path("<str:name>"), that path calls views.greet function and passes the string: name ("<str:name>") as a parameter for the views.greet function ==> becomes: "Hello, <str:name>!" "Hello, yourNameHere!"
# url looks like: examplesite.com/exampleApp1/yourName  or examplesite.com/exampleApp1/<str:name>
# examplesite.com/exampleApp1/Jenny ==> "Hello, Jenny!"
