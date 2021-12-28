from django.shortcuts import render
from types import CodeType
from django.shortcuts import render
from rest_framework import generics, serializers, status
from .serializers import RegisterTutorSerializer
from .models import Tutors
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
import uuid

# Create your views here.


class TutorsCreateView(generics.GenericAPIView):
    serializer_class = RegisterTutorSerializer
    def post(self, request):
     serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
     if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
     return Response({"status": "success", "data": "Item Created"})

