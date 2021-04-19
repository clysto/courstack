from rest_framework import permissions


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


class IsStudentPermission(permissions.BasePermission):
    message = "You are not a student."

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_student()
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    检查是否为课程的创建者
    """

    message = "You are not the owner."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.teacher == request.user.teacher
