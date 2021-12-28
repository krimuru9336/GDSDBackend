from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Tutors(models.Model):
    tutor_user_name = models.CharField(null=False,max_length=30)
    tutor_first_name = models.CharField(null=False,max_length=30)
    tutor_last_name = models.CharField(null=False,max_length=30)
    tutor_email = models.CharField(max_length=255,unique=True)
    tutor_address = models.CharField(max_length=255,unique=True)
    tutor_DOB = models.DateField(max_length=255,unique=True)
    tutor_registration_date = models.DateField(max_length=255,unique=True)
    tutor_phone_number = models.DateField(max_length=255,unique=True)
   
   # tutor_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


