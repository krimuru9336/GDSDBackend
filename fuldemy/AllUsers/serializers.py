from .models import FuldemyUser
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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


class TutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['email','first_name','last_name','address','DOB','phone_number','profile_pic','password','CV']

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
        fields = ['email','first_name','last_name','address','DOB','phone_number','profile_pic','password','CV','token']

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
        fields = ['email','first_name','last_name','address','DOB','phone_number', 'password','token','profile_pic']

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuldemyUser
        fields = ['profile_pic','DOB','phone_number','first_name','last_name','address','email']       