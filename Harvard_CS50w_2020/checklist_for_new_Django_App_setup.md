## Checklist for new Django app

1. in terminal: cd to desired location for default files. run 
	python manage.py startapp <nameOfApp>

to create default file structure for app
2.  in project folder: settings.py, add the new app's name to INSTALLED_APPS list
3. in project folder: in views.py add the path to the new app within urlpatterns:

	path('tasks', include("tasks.urls"))

4. inside of the new app's folder structure, create a new urls.py (that was linked to the project's urls.py in the last step)
5. app's urls.py copy structure from an example urls.py, it will have an index() function
6. in the app's views.py, create an index() function
7. see examples for more structure/copy
8. within the app structure: .html files go into the TEMPLATES folder and .css files go into the STATIC folder
9. any new .html templates/pages need to have a path() written into the urls.py located within the APP folder


- if you find yourself copy/pasting code from page to page, think "There's probably abetter way to do this"
