from django.db import models
from django.contrib.auth.models import User

class Student(User):
    bio = models.TextField()

class Teacher(User):
    bio = models.TextField()
class Department(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,blank=False)

class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,blank=False)
    desc = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

