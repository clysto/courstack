from .models import User, Course, Teacher, Student
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Student


class CourseSerializer(serializers.ModelSerializer):
    teacher = StudentSerializer()

    class Meta:
        model = Course
        fields = "__all__"
