from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]

# when you go to the path "add" example.com/tasks/add, the path function will call views.add function in views.py, which will render/display the task/add.html
