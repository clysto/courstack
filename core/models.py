from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    def is_student(self):
        return bool(Student.objects.filter(username=self.username).count())

    def is_teacher(self):
        return bool(Teacher.objects.filter(username=self.username).count())


class Student(User):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(User):
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Course(models.Model):
    description = models.CharField(max_length=128)
    date_start = models.DateField()
    date_stop = models.DateField()
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="teachers"
    )
    students = models.ManyToManyField(Student, related_name="students", blank=True)
