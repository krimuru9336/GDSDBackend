from django.urls import path

from .views import RegistrationAPIView,RegistrationStudentAPIView,TutorsView,FilteredTutorsView,UserAvatarUpload,ActiveClassesView,SkillsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authentication'


urlpatterns = [
    path('tutor/register', RegistrationAPIView.as_view()),
    path('auth/login/',TokenObtainPairView.as_view(),name='token'),
    #path('auth/login1', LoginView.as_view()),
    path('student/register', RegistrationStudentAPIView.as_view()),
    path(r'tutor/list/', TutorsView.as_view()),
    path(r'tutor/',FilteredTutorsView.as_view()),
    path(r'user/detail',UserAvatarUpload.as_view()),
    #path('update-user', ChangePasswordView.as_view()),
     path('skills',SkillsView.as_view()),
   path('skills/<int:id>',SkillsView.as_view()),
    ################################################################################
    #Kritika's urls
    path('reviews',ActiveClassesView.as_view()),
    path('reviews/<int:id>',ActiveClassesView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
