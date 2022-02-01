from .models import FuldemyUser,ActiveClasses,Skills
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer, CharField
from .models import MessageModel
from django.shortcuts import get_object_or_404





'''
class  MyTokenObtainPairSerializer(TokenObtainPairSerializer):
     def validate(self, attr):
         data=super().validate(attr)
         refresh = self.get_token(self.user)
         data['refresh'] = str(refresh)
         data['access'] = str(refresh.access_token)
         role='None'
         obj = FuldemyUser.objects.get(user=self.user)
         if obj.is_student==True:
            role='Student'
         if obj.is_student==True:
            role='Tutor'
         data["role"] = role
         return data
'''        


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id','skill_name','skill_type']
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['id','email','first_name','last_name','skills_present','skills_text','profile_pic']

class DetailauthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['id','email','first_name','last_name','address','DOB','phone_number','CV','skills_present','skills_text','profile_pic']


class TutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['id','email','first_name','last_name','address','DOB','phone_number','password','CV','skills_present','skills_text','is_student','is_teacher']

class RegistrationTutorSerializer(serializers.ModelSerializer):

    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = FuldemyUser
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id','email','first_name','last_name','address','DOB','phone_number','profile_pic','password','CV','token','skills_present']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return FuldemyUser.objects.create_tutor(**validated_data)




class RegistrationStudentSerializer(serializers.ModelSerializer):

    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = FuldemyUser
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id','email','first_name','last_name','address','DOB','phone_number', 'password','token','profile_pic']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return FuldemyUser.objects.create_student(**validated_data)


class RegistrationAdminSerializer(serializers.ModelSerializer):

    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = FuldemyUser
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email','first_name','last_name','address','DOB','phone_number', 'password','token','profile_pic','CV']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return FuldemyUser.objects.create_supeeruser(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(email=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'token': user.token
        }

class Serializer_UpdateUser(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ('DOB')


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['id','profile_pic','DOB','phone_number','first_name','last_name','address','email','password','skills_present','skills_text','CV','profile_pic','is_student','is_teacher'] 

################################Krithika################################################

#Kritika's code
class ActiveClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveClasses
        fields = ['id','class_id','tutor_id','student_id','skill_id','class_start_date','class_review','rating_by_student','feedback_in_words']

class GetByTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveClasses
        fields =  ['id','class_id','tutor_id','student_id','skill_id','class_start_date','class_review','rating_by_student','feedback_in_words']

class CreateActiveClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveClasses
        fields = ['id','class_id','tutor_id','student_id','skill_id','class_start_date','class_review','rating_by_student','feedback_in_words']

class UpdateActiveClassesSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])
    class Meta:
        model = ActiveClasses
        fields = ['id','class_id','tutor_id','skill_id','admin_id','class_start_date','skill_duration_left','class_description','rating_by_student','feedback_in_words']


################################  Syed   ################################################

class MessageModelSerializer(ModelSerializer):
    user = CharField(source='user.email', read_only=True)
    recipient = CharField(source='recipient.email')

    def create(self, validated_data):
        user = self.context['request'].user
        recipient = get_object_or_404(
            FuldemyUser, email=validated_data['recipient']['email'])
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)
        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient', 'timestamp', 'body')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ('email','first_name', 'last_name', 'id', 'profile_pic')
