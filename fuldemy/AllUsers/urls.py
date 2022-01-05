from django.urls import path

from .views import RegistrationAPIView,RegistrationStudentAPIView,UserAvatarUpload,TutorsView,FilteredTutorsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authentication'


urlpatterns = [
    path('tutor/register', RegistrationAPIView.as_view()),
    path('auth/login/',TokenObtainPairView.as_view(),name='token'),
    #path('auth/login1', LoginView.as_view()),
    path('student/register', RegistrationStudentAPIView.as_view()),
    path('tutor/list', TutorsView.as_view()),
    path(r'tutor/',FilteredTutorsView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
