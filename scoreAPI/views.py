from scoreAPI.serializers import UpdateStudentAssignmentSerializer
from scoreAPI.models import Assignment, Course, StudentAssignments
from scoreAPI.serializers import CourseSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from scoreAPI.permissions import TeacherRequired, StudentRequired
from django.contrib.auth import get_user_model 
from scoreAPI.serializers import UserSerializer, AssignmentSerializer, TeacherSerializer, StudentAssignmentsSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = UserSerializer

class CreateTeacherView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = TeacherSerializer

class CreateCourseView(CreateAPIView):

    model = Course
    permission_classes = [
        TeacherRequired
    ]
    serializer_class = CourseSerializer


class CreateAssignment(CreateAPIView):

    model = Assignment
    permission_classes = [
        TeacherRequired
    ]
    serializer_class = AssignmentSerializer


class sendAssignment(generics.CreateAPIView):
    queryset = StudentAssignments.objects.all()
    serializer_class = StudentAssignmentsSerializer
    permission_classes = [StudentRequired]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class gradeAssignment(generics.UpdateAPIView):

    queryset = StudentAssignments.objects.all()
    serializer_class = UpdateStudentAssignmentSerializer
    permission_classes = [
        TeacherRequired
    ]
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)



