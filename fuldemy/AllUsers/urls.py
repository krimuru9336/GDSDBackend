from django.urls import path

from .views import RegistrationAPIView,LoginAPIView,RegistrationStudentAPIView,UserAvatarUpload
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authentication'


urlpatterns = [
    path('tutor/register', RegistrationAPIView.as_view()),
    #path('login/',TokenObtainPairView.as_view(),name='login'),
    path('auth/login', LoginAPIView.as_view()),
    path('student/register', RegistrationStudentAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
