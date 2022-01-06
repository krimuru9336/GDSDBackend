from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'posts/{filename}'.format(filename=filename)

def CV_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'CV/{filename}'.format(filename=filename)


class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,address,DOB,phone_number,profile_pic,CV, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not CV:
           CV=None

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            DOB=DOB,
            phone_number=phone_number,
            profile_pic=profile_pic,
            CV=CV
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_student(self, email,first_name,last_name,address,DOB,phone_number,profile_pic,CV=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            DOB=DOB,
            phone_number=phone_number,
            profile_pic=profile_pic,
            CV='settings.MEDIA_ROOT/CV/Sourajyoti_Datta_CV.pdf'
            
        )
        user.is_student = True
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_tutor(self, email,first_name,last_name,address,DOB,phone_number,profile_pic,CV, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            DOB=DOB,
            phone_number=phone_number,
            profile_pic=profile_pic,
            CV=CV
             )
        user.is_teacher = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,first_name,last_name,address,DOB,phone_number,profile_pic,CV, password):

      user = self.create_user(
              email=email,
              first_name=first_name,
              last_name=last_name,
              address=address,
              DOB=DOB,
              phone_number=phone_number,
              profile_pic=profile_pic,
              password=password,
              CV=CV
              )
      user.is_admin = True
      user.is_staff=True
      user.is_superuser = True
      user.save(using=self._db)
      return user



# Create your models here.
class FuldemyUser(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(verbose_name="email",max_length=50,unique=True)
        first_name = models.CharField(null=False,max_length=30)
        last_name = models.CharField(null=False,max_length=30)
        address = models.CharField(max_length=255)
        DOB = models.DateField(max_length=255)
        registration_date = models.DateTimeField(auto_now=True)
        phone_number = models.IntegerField(unique=True)
        is_admin= models.BooleanField(default=False)
        is_superuser= models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_student= models.BooleanField(default=False)
        is_teacher= models.BooleanField(default=False)
        profile_pic = models.ImageField(upload_to =user_directory_path,default='default.jpg')
        CV = models.FileField(upload_to =CV_directory_path,default='settings.MEDIA_ROOT/CV/Sourajyoti_Datta_CV.pdf')
        #CV = models.CharField(max_length=255,default='None',editable=True)

        objects = UserManager()

        USERNAME_FIELD="email"


        REQUIRED_FIELDS=['first_name','last_name','address','DOB','phone_number','profile_pic','CV']

        def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
         return True
        
        def __str__(self):
         return self.email


        

''' @property
        def token(self):
        
         return self._generate_jwt_token()
        
        def _generate_jwt_token(self):

          dt = datetime.now() + timedelta(days=60)
          key = "secret"
          token = jwt.encode(
              {
                'id': self.pk,
                "exp": dt
               },settings.SECRET_KEY, algorithm='HS256')

          #return jwt.decode(token,settings.SECRET_KEY, algorithms='HS256')
          return token'''

'''class user_type(models.Model):
     is_teach = models.BooleanField(default=False)
     is_student = models.BooleanField(default=False)
     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

     def __str__(self):
         if self.is_student == True:
             return MyUser.get_email(self.user) + " - is_student"
         else:
             return MyUser.get_email(self.user) + " - is_teacher"'''

