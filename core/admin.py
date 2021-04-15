from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Course, Student, Teacher, CourseSection, Attachment

admin.site.register(User, UserAdmin)
admin.site.register(CourseSection)
admin.site.register(Attachment)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
