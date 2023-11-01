from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

# for each path created in urlpatterns, you need to make a corresponding function within views.py