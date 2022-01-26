from django.urls import path

from .views import RegistrationAPIView,RegistrationStudentAPIView,TutorsView,FilteredTutorsView,UserAvatarUpload,ActiveClassesView,SkillsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .api import MessageModelViewSet, UserModelViewSet



router = DefaultRouter()
router.register(r'message', MessageModelViewSet, basename='message-api')
router.register(r'user', UserModelViewSet, basename='user-api')




app_name = 'authentication'


urlpatterns = [
    path('tutor/register', RegistrationAPIView.as_view()),
    path('auth/login/',TokenObtainPairView.as_view(),name='token'),
    #path('auth/login1', LoginView.as_view()),
    path('student/register', RegistrationStudentAPIView.as_view()),
    path(r'tutor/list/', TutorsView.as_view()),
    path(r'tutor/',FilteredTutorsView.as_view()),
    path(r'user/detail',UserAvatarUpload.as_view()),
     path('skills',SkillsView.as_view()),
   path('skills/<int:id>',SkillsView.as_view()),
    ####################### Chat #########################################################
    path('', login_required(
        TemplateView.as_view(template_name='core/chat.html')), name='home'),
    path(r'messageurl/', include(router.urls)),
  ####################### Krithika #########################################################

    path('reviews',ActiveClassesView.as_view()),
    path('reviews/<int:id>',ActiveClassesView.as_view()),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
