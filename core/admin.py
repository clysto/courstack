from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Student, Teacher


class TeacherAdmin(admin.ModelAdmin):
    fields = ("username", "email")


admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher, TeacherAdmin)
