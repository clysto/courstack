from django.urls import path, include
from django.conf import settings
from rest_framework_nested import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"courses", views.CourseViewSet, basename="course")
router.register(r"teachers", views.TeacherViewSet, basename="teacher")
router.register(r"students", views.StudentViewSet, basename="student")

teachers_router = routers.NestedDefaultRouter(router, r"teachers", lookup="teacher")
teachers_router.register(r"courses", views.TeacherCourseViewSet, basename="teacher-course")

students_router = routers.NestedDefaultRouter(router, r"students", lookup="student")
students_router.register(r"courses", views.StudentCourseViewSet, basename="student-course")

courses_router = routers.NestedDefaultRouter(router, r"courses", lookup="course")
courses_router.register(r"sections", views.CourseSectionViewSet, basename="course-section")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
    path("", include(teachers_router.urls)),
    path("", include(students_router.urls)),
    path("", include(courses_router.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path("auth/", include("rest_framework.urls")),
    ]
