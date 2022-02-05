# GDSDBackend

## APIs

### Reviews

POST - http://127.0.0.1:8000/api/reviews

  Give rating, feedback and review null
  

GET all data - http://127.0.0.1:8000/api/reviews


PATCH - http://127.0.0.1:8000/api/reviews/1_2

  give classid in URL

  class_id = <tutor_id>_<student_id>
  

GET by class_id = http://127.0.0.1:8000/api/reviews/1_2
	
  give class_id in URL
  

GET by tutor_id = http://127.0.0.1:8000/api/reviews/getByTutor/2

  give tutor_id in URL
  

DELETE by class_id = http://127.0.0.1:8000/api/reviews/1_2

  give class_id in URL
  
  ADMIN rest api

Get all tutors with is_active_tutor field as false = http://127.0.0.1:8000/api/checkCV/

Patch by email = http://127.0.0.1:8000/api/checkCV/?email=kritutor1@hs-fulda.de

give email in URL ?email=arya1@hs-fulda.de

GET by email = http://127.0.0.1:8000/api/checkCV/?email=arya1@hs-fulda.de

give email in URL ?email=arya1@hs-fulda.de


## Download and install
https://www.memurai.com/

## installations required in the system

pip install django-extensions

pip install -U djoser

pip install djangorestframework-simplejwt

pip install Pillow

pip install --user django-cors-headers

python -m pip install -U channels

pip install channels-redis==2.4.2


## Steps to create and start the project

django-admin startproject fuldemy

python3 manage.py startapp AllUsers	

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py makemigrations AllUsers

python3 manage.py migrate AllUsers

python3 manage.py createsuperuser

