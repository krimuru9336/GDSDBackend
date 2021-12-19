from types import CodeType
from django.shortcuts import render
from rest_framework import generics, serializers, status
from .serializers import TutorsSerializer, CreateTutorSerializer, UpdateTutorSerializer,TutorsPostSerializer
from .models import Tutors
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
# def main(request):
#     return HttpResponse("<h1 style='color:blue;'>Hello</h1>")


class TutorsCreateView(generics.CreateAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorsSerializer



class TutorsView(APIView):
    def get(self,request,id=None):
     if id: 
         item = Tutors.objects.get(id=id)
         serializer = TutorsSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     queryset = Tutors.objects.all()
     serializer_class = TutorsSerializer(queryset,many=True)
     return Response(serializer_class.data)
    def post(self, request):
        serializer = TutorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        item = Tutors.objects.get(id=id)
        serializer = TutorsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    def delete(self, request, id=None):
        item = get_object_or_404(Tutors, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class GetFilteredTutorsView(APIView):
    def get(self, request,*args):
      
      tutor_first_name=request.query_params["tutor_first_name"]
      print(tutor_first_name)
      queryset1 = Tutors.objects.get(tutor_first_name=tutor_first_name)
      if request.method == 'GET': 
       serializer_class = TutorsSerializer(queryset1)
       return Response(serializer_class.data)
    def delete(self, request,*args):
        tutor_first_name=request.query_params["tutor_first_name"]
        Tutors.objects.filter(tutor_first_name=tutor_first_name).delete()
        return Response({"message": "Tutor has been deleted."},status=204)
    def patch(self, request,*args):
        tutor_first_name=request.query_params["tutor_first_name"]
        Tutors.objects.filter(tutor_first_name=tutor_first_name).delete()
        return Response({"message": "Tutor has been updated."},status=204)
class FilteredTutorsView(generics.ListAPIView):
     queryset = Tutors.objects.all()
     serializer_class = TutorsSerializer
     filter_backends = [SearchFilter, OrderingFilter]
     search_fields = ['tutor_first_name', 'tutor_last_name','tutor_email']
