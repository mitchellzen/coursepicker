# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from course_picker.models import Course, Professor, Session

class ProfessorInline(admin.TabularInline):
    model = Course.professors.through

class SessionInline(admin.TabularInline):
    model = Session

class CourseAdmin(admin.ModelAdmin):
    inlines = (ProfessorInline, SessionInline)

admin.site.register(Professor)
admin.site.register(Course, CourseAdmin)