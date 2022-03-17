from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import (Model, TextField, DateTimeField, ForeignKey,
                              CASCADE)


#######Debarati Code##################################################
def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'posts/{filename}'.format(filename=filename)

def CV_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'CV/{filename}'.format(filename=filename)

class Skills(models.Model):
    skill_name = models.CharField(null=False,max_length=30)
    skill_type = models.CharField(null=False,max_length=30)
    def __str__(self):
        return self.skill_name

class UserManager(BaseUserManager):
   # def create_user(self, email,first_name,last_name,address,DOB,phone_number,profile_pic=None,CV=None,skills_present=None , password=None):
    def create_user(self, email,first_name,last_name,address,DOB,phone_number,password=None,**extra_fields):

        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not extra_fields.get("CV"):
           CV=None
        else:
         CV=extra_fields.get("CV")
        if not extra_fields.get("profile_pic"):
           profile_pic=None
        else:
          profile_pic=extra_fields.get("profile_pic")
        if extra_fields.get("skills_present"):
         skills_text=str(extra_fields.get("skills_present"))
         x = skills_text.replace(">", "").split(", ")
         str1=""
         for i in x:
           sub=i.split(": ")[1]
           str1=str1+","+sub
         skills_text = str1[1:].replace("]", "")
        else:
          skills_text=""

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            DOB=DOB,
            phone_number=phone_number,
            profile_pic=profile_pic,
            CV=CV,
            skills_text=skills_text
        )
        user.set_password(password)
        user.save(using=self._db)
        if  extra_fields.get("skills_present"):
         for i in extra_fields.get("skills_present"): 
          user.skills_present.add(i)
        #user.skills_present.add(skills_present[1])
        
        return user

    def create_student(self, email,first_name,last_name,address,DOB,phone_number, password=None,**extra_fields):
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
            profile_pic=extra_fields.get("profile_pic"),
            CV='settings.MEDIA_ROOT/CV/Sourajyoti_Datta_CV.pdf',
            skills_present=extra_fields.get("skills_present")

            
        )
        user.is_student = True
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_tutor(self, email,first_name,last_name,address,DOB,phone_number,password,**extra_fields):
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
            profile_pic=extra_fields.get("profile_pic"),
            CV=extra_fields.get("CV"),
            skills_present=extra_fields.get("skills_present")
             )
        user.is_teacher = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,first_name,last_name,address,DOB,phone_number, password,**extra_fields):

      user = self.create_user(
              email=email,
              first_name=first_name,
              last_name=last_name,
              address=address,
              DOB=DOB,
              phone_number=phone_number,
              profile_pic=extra_fields.get("profile_pic"),
              password=password,
              CV=extra_fields.get("CV"),
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
        is_active_teacher= models.BooleanField(default=False)
        profile_pic = models.ImageField(upload_to =user_directory_path,default='default.jpg',blank=True)
        CV = models.FileField(upload_to =CV_directory_path,default='settings.MEDIA_ROOT/CV/Sourajyoti_Datta_CV.pdf',blank=True)
        #CV = models.CharField(max_length=255,default='None',editable=True)
        skills_present = models.ManyToManyField('AllUsers.Skills',blank=True, null=True)
        #skills_present = models.ForeignKey(Skills, on_delete=models.CASCADE)
        skills_text = models.CharField(max_length=255,default="",blank=True)

        objects = UserManager()

        USERNAME_FIELD="email"


        REQUIRED_FIELDS=['first_name','last_name','address','DOB','phone_number']


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

class TimeTable(models.Model):
    DAYS_OF_THE_WEEK = (
        ('1', 'SUNDAY'),
        ('2', 'MONDAY'),
        ('3', 'TUESDAY'),
        ('4', 'WEDNESDAY'),
        ('5', 'THURSDAY'),
        ('6', 'FRIDAY'),
        ('7', 'SATURDAY')
    )
    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=1, choices=DAYS_OF_THE_WEEK)
    
    def __str__(self):
        return self.get_day_display()

    class Meta:
        verbose_name = 'TIMETABLE'
        verbose_name_plural = 'TIMETABLE'
class TimeTableItem(models.Model):
    #time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    #subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(FuldemyUser, on_delete=models.CASCADE)
    time_table = models.ManyToManyField(TimeTable,blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    #def __str__(self):
        #return 'timetable:'.format(self.subject, self.teacher, self.start_time, self.end_time)

    #class Meta:
        #ordering = ('start_time',)

################################################################################

#Kritika's code

class ActiveClasses(models.Model):
    class_id = models.CharField(null=False, unique=True, max_length=30) #primary key
    tutor_id = models.IntegerField(null=False) #Comes from FuldemyUser table
    student_id =  models.IntegerField(null=False) #Comes from FuldemyUser table 
    skill_id = models.IntegerField(null=False)  #Comes from FuldemyUser table
    class_start_date = models.DateField(null=False) #Add current date
    #skill_duration_left = models.IntegerField() #Comes from Skills table
    class_review = models.CharField(max_length=255, null=True) #Updated from UI
    rating_by_student = models.IntegerField(null=True) #Updated from UI
    feedback_in_words = models.CharField(max_length=1000, null=True) #Updated from UI




####################Syed Chat code#########################################################
class MessageModel(Model):
    """
    This class represents a chat message. It has a owner (user), timestamp and
    the message body.

    """
    user = ForeignKey(FuldemyUser, on_delete=CASCADE, verbose_name='user',
                      related_name='from_user', db_index=True)
    recipient = ForeignKey(FuldemyUser, on_delete=CASCADE, verbose_name='recipient',
                           related_name='to_user', db_index=True)
    timestamp = DateTimeField('timestamp', auto_now_add=True, editable=False,
                              db_index=True)
    body = TextField('body')

    def __str__(self):
        return str(self.id)

    def characters(self):
        """
        Toy function to count body characters.
        :return: body's char number
        """
        return len(self.body)

    def notify_ws_clients(self):
        """
        Inform client there is a new message.
        """
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }

        channel_layer = get_channel_layer()


        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        """
        Trims white spaces, saves the message and notifies the recipient via WS
        if the message is new.
        """
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    # Meta
    class Meta:
        app_label = 'AllUsers'
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)

