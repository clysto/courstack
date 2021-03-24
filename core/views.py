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
from .permissions import IsTeacherOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Course


class TeacherViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    lookup_field = "account__username"
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class StudentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    lookup_field = "account__username"
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        teacher = self.request.query_params.get("teacher", None)
        if teacher is not None:
            queryset = queryset.filter(teacher__account__username=teacher)
        return queryset


class TeacherCourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Course.objects.filter(teacher__account__username=self.kwargs["teacher_account__username"])

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacher)
