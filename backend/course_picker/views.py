# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django_tables2 import tables, RequestConfig
from rest_framework import viewsets
from .permissions import IsStaffOrTargetUser   
from rest_framework.permissions import AllowAny
from course_picker.models import Course
from course_picker.serializers import UserSerializer, CourseSerializer
from django.shortcuts import render


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User


def get_permissions(self):
    # allow non-authenticated user to create via POST
    return (AllowAny() if self.request.method == 'POST'
    else IsStaffOrTargetUser()),


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    model = Course


class CourseTable(tables.Table):
    id = tables.columns.TemplateColumn('<a href="/courses/{{ value }}">{{value}}</a>')
    class Meta:
        model = Course
        row_attrs = {
            'data-id': lambda record: record.pk
        }


def courses(request):
    table = CourseTable(Course.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'courses.html', {'courses': table})


#todo enroll in course
def course(request, course_id):
    return render(request, 'course.html', {'course': Course.objects.get(id=course_id)})
