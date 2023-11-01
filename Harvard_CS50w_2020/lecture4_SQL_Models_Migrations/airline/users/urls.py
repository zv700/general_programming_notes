from django.urls import path

from . import views # from . means from within the current folder --> users/views.py

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]
# index, login_view, and logut_view are functions within views.py
