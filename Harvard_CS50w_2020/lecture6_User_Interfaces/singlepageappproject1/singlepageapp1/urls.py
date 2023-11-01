#this app level urls.py is not present by default, needs to be created manually for each app
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    ## default path, loads the index page 
    path("sections/<int:num>", views.section, name="section")   # path/url loads a specfic section of a page -> go to views.py for section info
]