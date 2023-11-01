import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
        #"newyear": True
    })

# logic checks if today's date is New Years Day/ January 1st when the .html template is accessed by the client/user
# "newyear" = variable that gives boolean True or False based on if both "now" statements are true, 
# if both "now" statements are true then "newyear" = True, if both are false or at least one is false then "newyear" = False
    # "now.month == 1" checks to see if the current month is January (month: 1)
    # "and" tells Python to check for both statements T or F
    # "now.day == 1" checks to see if the current day is the first of the month

# Python default module "datetime" has a function called "datetime" that checks for date and time = datetime[the module].datetime[the function]
    # the "now()" in datetime.datetime.now() stores the boolean T or F answer from variable "newyear"

# .css style sheet file is a static file = a file that will not change
# .html template is not a static file, Django can make changes dynamically through logic
# static folder within app will contain all static files