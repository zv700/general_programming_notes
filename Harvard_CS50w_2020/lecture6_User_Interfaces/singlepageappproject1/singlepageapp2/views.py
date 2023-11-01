from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepageapp2/index.html")

texts = ["This is example placeholder content text for an example page of a single page app.",
         "You could have spent that $30 on fried chicken. Idiot.",
         "I'm hungry."]

# checks if number is between 1 and 3, then responds with a string of text from: texts
def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else: 
        raise Http404("No such section")