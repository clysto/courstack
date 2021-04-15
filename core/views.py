from rest_framework.decorators import action
from rest_framework.serializers import Serializer

from .models import Teacher, Student
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework import mixins

from .response import APIResponse
from .serializers import (
    TeacherSerializer,
    CourseSerializer,
    StudentSerializer,
)
from .permissions import IsTeacherOrReadOnly, IsOwnerOrReadOnly, IsStudentPermission
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

    def get_queryset(self):
        queryset = Course.objects.all()
        teacher = self.request.query_params.get("teacher", None)
        if teacher is not None:
            queryset = queryset.filter(teacher__account__username=teacher)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsStudentPermission])
    def select(self, request, pk=None):
        """
        学生选课
        """
        course = self.get_object()
        user = request.user
        course.students.add(user.student)
        return APIResponse("select successful.")

    def get_serializer_class(self):
        if self.action == 'select':
            return Serializer
        return CourseSerializer


class TeacherCourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Course.objects.filter(teacher__account__username=self.kwargs["teacher_account__username"])

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacher)


class StudentCourseViewSet(ReadOnlyModelViewSet):
    """
    显示所有学生已选课程
    """
    serializer_class = CourseSerializer
    permission_classes = [IsStudentPermission]

    def get_queryset(self):
        return Course.objects.filter(students__account__username__contains=self.kwargs["student_account__username"])


class CourseActionViesSet(GenericViewSet):
    permission_classes = [IsStudentPermission]

    @action(detail=True, methods=['post'])
    def select_course(self):
        print(123)
        pass
