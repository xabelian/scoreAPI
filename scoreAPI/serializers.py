from asyncore import read
from rest_framework import serializers
from scoreAPI.models import Teacher, Assignment, Course,  StudentAssignments
from scoreAPI.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_student = True
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )


class TeacherSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_teacher = True
        )
        teacher = Teacher.objects.create(user=user)
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name']

    def create(self, validated_data):
        course = Course.objects.create(
            course_name = validated_data['course_name'],
            teacher = Teacher.objects.get(pk=self.context['request'].user)
        )
        return course


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['course', 'title']

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)

class StudentAssignmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentAssignments
        fields = ['assignment', 'score', 'comment']
    def create(self, validated_data):
        student_assignment = StudentAssignments.objects.create(
                assignment = validated_data['assignment'],
                student = self.context['request'].user,
                comment = validated_data['comment'],
            )
        return student_assignment


class UpdateStudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssignments
        fields = ['score']

    def update(self, instance, validated_data):

        student_assignment = StudentAssignments.objects.get(pk=instance.id)
        student_assignment.score = validated_data['score']
        student_assignment.save()
        return student_assignment



    
    

