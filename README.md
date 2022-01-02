# GDSDBackend


installations required in the system
-------------------------------------------------------
pip install django-extensions
pip install -U djoser
pip install djangorestframework-simplejwt
pip install Pillow
pip install --user django-cors-headers

Steps to create and start the project
----------------------------------------

django-admin startproject fuldemy
py manage.py startapp AllUsers	

py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser

