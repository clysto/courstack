from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    def is_student(self):
        return hasattr(self, "student")

    def is_teacher(self):
        return hasattr(self, "teacher")


class Student(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.account.username


class Teacher(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.account.username


class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    date_start = models.DateField()
    date_end = models.DateField()
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="teachers"
    )
    students = models.ManyToManyField(Student, related_name="students", blank=True)

    def __str__(self):
        return self.name
