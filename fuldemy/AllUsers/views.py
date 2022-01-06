from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from rest_framework import generics, serializers, status
from .serializers import RegistrationTutorSerializer,RegistrationStudentSerializer,UserSerializer,TutorsSerializer,RegistrationAdminSerializer

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from .models import FuldemyUser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



class FilteredTutorsView(generics.ListAPIView):
     permission_classes = (AllowAny,)
     queryset = FuldemyUser.objects.all()
     serializer_class = TutorsSerializer
     filter_backends = [SearchFilter, OrderingFilter]
     search_fields = ['email', 'first_name','last_name']


class TutorsView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
     '''if id: 
         item = FuldemyUser.objects.get(email=id)
         serializer = TutorsSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)     '''
     queryset = FuldemyUser.objects.filter(is_teacher=True).all()
     serializer_class = TutorsSerializer(queryset,many=True)
     return Response(serializer_class.data)
class RegistrationAPIView(generics.GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationTutorSerializer

    def post(self, request):
        #user = request.data.get('user', {})
        serializer = self.get_serializer(data = request.data)


        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": "success", "data": "Teacher Registered"})
        else:
         return Response({"status": "error", "data": serializer.errors})  

class RegistrationTutorView(generics.GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationAdminSerializer

    def post(self, request):
        #user = request.data.get('user', {})
        serializer = self.get_serializer(data = request.data)


        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": "success", "data": "Teacher Registered"})
        else:
         return Response({"status": "error", "data": serializer.errors})  

        
        

class RegistrationStudentAPIView(generics.GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationStudentSerializer

    def post(self, request):
        #user = request.data.get('user', {})
        serializer = self.get_serializer(data = request.data)
        data={}

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        if(serializer.is_valid()):
            serializer.save()
            '''refresh=RefreshToken.for_user(FuldemyUser)
            data['token']={
                            'refresh': str(refresh),
                             'access': str(refresh.access_token),

                           }
            data['response']="Registration successful"
            data['email']= FuldemyUser.email'''
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
        else:
          return Response({"status": "error", "data": serializer.errors})     
        
        #return Response({"status": data['response'] , "token informations":data['token'] })
        #return Response(data)
        

'''
class LoginView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer
'''



'''class LoginAPIView(generics.GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        #user = request.data.get('user', {})
        serializer = self.get_serializer(data = request.data)

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"status": "success", "data": "User Logged in"})'''



class UserAvatarUpload(APIView):
    permission_classes = (AllowAny,)
    parsers_classes= [MultiPartParser, FormParser]
    ''' def patch(self, request,email=None):
        item = FuldemyUser.objects.get(email=email)
        serializer = UserSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)''' 
    def put(self, request):
        serializer = UserSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

