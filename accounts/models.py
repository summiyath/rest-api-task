from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_number = models.IntegerField
    standard = models.TextField(max_length= 20)
    date_created = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    subject = models.CharField(max_length= 20)
    phone_number = models.IntegerField
    date_created = models.DateTimeField(auto_now=True)

    student =models.ForeignKey(Student,on_delete=models.CASCADE)


