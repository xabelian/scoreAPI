from rest_framework import permissions

class TeacherRequired(permissions.BasePermission):
    """
    Custom permission class used in views that should only be used by Teachers (Create Course, Create Assignment, Grade Assignment).
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_teacher:
            return True

class StudentRequired(permissions.BasePermission):
    """
    Custom permission class used in the Send Assignment view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_student:
            return True

    