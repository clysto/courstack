from .models import User, Course, Teacher, Student, CourseSection, Attachment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    account = UserSerializer()

    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    account = UserSerializer()

    class Meta:
        model = Student
        fields = "__all__"


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ["file", "name"]


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    sections = serializers.HyperlinkedIdentityField(
        view_name="course-section-list", lookup_url_kwarg="course_pk"
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "date_start",
            "date_end",
            "teacher",
            "sections",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }


class CourseSectionSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = CourseSection
        fields = ["id", "date", "content", "attachments"]
