from django.shortcuts import render
from django.http import JsonResponse

import time

# Create your views here.

def index(request):
    return render(request, "posts/index.html")

def posts(request):
    # make an api: presents posts in a JavaScript object
    # when making a request to /posts, you need 2 arguments: start and end
    # to test: runserver and try the url "/posts?start=1&end=10"


    # Get start and end points [what post you want to start with, what post you want to end with]
    start = int(request.Get.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    #Generate list of posts [generate a list of sample posts, "post #1, post #2, etc."]
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    #Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })