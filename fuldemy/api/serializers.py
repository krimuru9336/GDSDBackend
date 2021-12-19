from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Tutors

class TutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ['id','tutor_first_name','tutor_last_name','tutor_email']

class TutorsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ['id','tutor_first_name','tutor_last_name','tutor_email']        

class CreateTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ('tutor_first_name','tutor_last_name','tutor_email')

class UpdateTutorSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])
    class Meta:
        model = Tutors
        fields = ('id','tutor_first_name','tutor_last_name','tutor_email')