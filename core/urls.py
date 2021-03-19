from django.urls import path, include
from django.conf import settings
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

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path("auth/", include("rest_framework.urls")),
    ]
