from rest_framework import permissions
from .models import User


class IsTeacherPermission(permissions.BasePermission):
    message = "You are not a teacher."

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_teacher()
        )


class IsTeacherOrReadOnly(permissions.BasePermission):
    message = "You are not a teacher."

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.is_teacher()
        )
