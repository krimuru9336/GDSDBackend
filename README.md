# GDSDBackend
download and install
https://www.memurai.com/

installations required in the system
-------------------------------------------------------
pip install django-extensions
pip install -U djoser
pip install djangorestframework-simplejwt
pip install Pillow
pip install --user django-cors-headers
python -m pip install -U channels
pip install channels-redis==2.4.2

Steps to create and start the project
----------------------------------------

django-admin startproject fuldemy
py manage.py startapp AllUsers	

py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser

