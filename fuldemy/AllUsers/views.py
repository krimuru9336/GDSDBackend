from rest_framework import status
from rest_framework.fields import EmailField
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from rest_framework import generics, serializers, status
from .serializers import ActiveClassesSerializer, RegistrationTutorSerializer,RegistrationStudentSerializer,TutorsSerializer,RegistrationAdminSerializer,UpdateUserSerializer

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from .models import ActiveClasses, FuldemyUser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import RetrieveUpdateAPIView



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

class UserView(APIView):
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
    permission_classes = (IsAuthenticated,)
    parsers_classes= [MultiPartParser, FormParser]
    serializer_class = UpdateUserSerializer
    serializer_class2=TutorsSerializer
    ''' def patch(self, request,email=None):
        item = FuldemyUser.objects.get(email=email)
        serializer = UserSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)''' 
    def get(self,request,*args):
        #email=request.query_params["email"]
         serializer = self.serializer_class(request.user)
     # item = FuldemyUser.objects.get(email=email)
       # serializer = TutorsSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer1 = self.serializer_class(request.user)
        email1=serializer1.data['email']
        #search=request.query_params["email"]
        item = FuldemyUser.objects.get(email=email1)
        serializer = UpdateUserSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



################################################################################
#Kritika's code


class ActiveClassesCreateView(generics.CreateAPIView):
    queryset = ActiveClasses.objects.all()
    serializer_class = ActiveClassesSerializer


class ActiveClassesView(APIView):
    def get(self,request,id=None):
     if id: 
         item = ActiveClasses.objects.get(id=id)
         serializer = ActiveClassesSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     queryset = ActiveClasses.objects.all()
     serializer_class = ActiveClassesSerializer(queryset,many=True)
     return Response(serializer_class.data)
    def post(self, request):
        serializer = ActiveClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        item = ActiveClasses.objects.get(id=id)
        serializer = ActiveClassesSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    def delete(self, request, id=None):
        item = generics.get_object_or_404(ActiveClasses, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})