"""
URL configuration for lecture3ExampleDjangoProject project.

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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exampleApp1/', include("exampleApp1.urls")),
    path('newyear/', include("newyear.urls")),
    path('tasks/', include("tasks.urls"))
]

# LINE 22: links urls.py within exampleApp1 app folder to this urls.py (that controls the urls for the entire project)
# LINE 22: link ALL of the urls within the exampleApp1 Django App folder using the include() function as the second argument to path()
# since you are using "include" in the path to 'exampleApp1' you must import "include" above from django.urls (LINE 18, next to paths)

# each app's urls.py is not created by default, you need to make it
