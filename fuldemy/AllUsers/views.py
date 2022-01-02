from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from rest_framework import generics, serializers, status
from .serializers import RegistrationTutorSerializer,LoginSerializer,RegistrationStudentSerializer,UserSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from .models import FuldemyUser

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
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"status": "success", "data": "Teacher Registered"})

class RegistrationStudentAPIView(generics.GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationStudentSerializer

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
        
        return Response({"status": "success", "data": "Student Registered"})


class LoginAPIView(generics.GenericAPIView):
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
        
        return Response({"status": "success", "data": "User Logged in"})



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

