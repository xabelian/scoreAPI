"""CourseSystem URL Configuration
"""

from django.urls import include, path
from rest_framework import routers
from scoreAPI.views import gradeAssignment, sendAssignment
from scoreAPI import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/create/', views.CreateUserView.as_view()),
    path('teachers/create/', views.CreateTeacherView.as_view()),
    path('courses/create/', views.CreateCourseView.as_view()),
    path('assignments/create/', views.CreateAssignment.as_view()),
    path('studentAssignment/send', sendAssignment.as_view()),
    path('studentAssignment/grade/<int:pk>', gradeAssignment.as_view())
]
