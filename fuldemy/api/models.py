from django.db import models

# Create your models here.
class Tutors(models.Model):
    tutor_first_name = models.CharField(null=False,max_length=30)
    tutor_last_name = models.CharField(null=False,max_length=30)
    tutor_email = models.CharField(max_length=255,unique=True)