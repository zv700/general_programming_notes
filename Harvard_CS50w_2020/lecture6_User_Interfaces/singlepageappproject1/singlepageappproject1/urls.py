"""
URL configuration for singlepageappproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('singlepageapp1.urls')), ## if "empty path didn't match any of these" error when accessing page after running server, include this line to specify a default html template route
    path('admin/', admin.site.urls),
    path('singlepageapp1/', include("singlepageapp1.urls")),
    path('singlepageapp2/', include("singlepageapp2.urls"))
]
