**To create a virtual environemnt, use** ```virtualenv -p python3 .``` 
**Then enter the virtual environment, and** ```pip install django```
**First starting off first run venv using** ```source bin/activate```
**To start a newDjango project, run** ```django-admin startproject django-project-name .```
**To run the server, run** ```python manage.py runserver```
**To run the database, run** ```python managy.py migrate``` --> syncs whatever settings and apps we have to the Django project.
**To create a user to have access to admin, run** ```python manage.py createsuperuser```, then you are able to login to localhost/admin
**To start your own app, run** ```python manage.py startapp app-name```
**After adding a model into your own app, make sure to write it in settings.py, and run** ```python manage.py makemigrations```, then ```python manage.py migrate```
> **To use a python interpreter to manage django stuff, use** ```python manage.py shell```, you can run python code such as: 
```
from products.models import Product
Product.objects.all()
Product.objects.create(title='New product 2', description='another one', price='1911', summary='sweet')
Product.objects.all()
```