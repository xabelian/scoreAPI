from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.timezone import now



class User(AbstractUser):
    """
    Custom implementation of User with boolean flags to differenciate the student-user(the "default" kind of user) and the
    teacher-user.
    """
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

class Teacher(models.Model):
    """
    The teacher model storages the primary keys of all teachers.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Course(models.Model):
    """
    The Course model has an assigned teacher.
    """
    course_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['course_name']

class Assignment(models.Model):
    """
    A Course has a set of assignments.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(User, through='StudentAssignments')
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
class StudentAssignments(models.Model):
    """
    Associative table that represents the many-to-many relation between Assignment and User (Students). 
    In other words, it represents the fact that a student can send/upload many assignments.
    The score is by default NULL until the assignment is graded by a teacher.
    """
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    upload_date = models.DateTimeField(default=now, blank=True)


