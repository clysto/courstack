from .models import User, Teacher, Student
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    TeacherSerializer,
    CourseSerializer,
    StudentSerializer,
)
from .permissions import IsTeacherOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Course


class TeacherViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    lookup_field = "username"
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class StudentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    lookup_field = "username"
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class CourseViewSet(ModelViewSet):
    # queryset = Course.objects.all()
    permission_classes = [IsTeacherOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        teacher = self.request.query_params.get("teacher", None)
        if teacher is not None:
            queryset = queryset.filter(teacher=teacher)
        return queryset
