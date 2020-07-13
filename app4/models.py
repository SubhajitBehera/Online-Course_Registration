


from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=30,unique=True)

class LoginModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

class ScheduleModel(models.Model):
    name=models.CharField(max_length=50,unique=True)
    faculty=models.CharField(max_length=30,primary_key=True)
    date=models.DateField()
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.IntegerField()

class Enroll(models.Model):
    cid = models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=20)
    faculty_name=models.CharField(max_length=20)