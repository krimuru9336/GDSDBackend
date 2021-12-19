from django.urls import path,include
from .views import TutorsView,FilteredTutorsView
#from .views import TutorsView, GetTutor, DeleteTutor, UpdateTutorView,GetFilteredTutorsView,TutorsCreateView

from rest_framework import routers
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

   path('tutors',TutorsView.as_view()),
   path('tutors/<int:id>',TutorsView.as_view()),
   path(r'tutors/',FilteredTutorsView.as_view()),
  # path('create-tutor',TutorsCreateView.as_view()),
  # path(r'tutor',GetFilteredTutorsView.as_view()),
  # path('get-tutor',GetTutor.as_view()),
  # path('delete-tutor',DeleteTutor.as_view()),
  # path('update-tutor',UpdateTutorView.as_view()),

]





