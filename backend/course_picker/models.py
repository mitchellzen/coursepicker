# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

#todo Course manager that allows sorting and pre-loading for efficiency

# Courses
class Course(models.Model):
    name = models.CharField(max_length=144)
    cost = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.name


class Professor(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=144)
    courses = models.ManyToManyField(Course, related_name="professors", blank=True)

    def save(self, *args, **kwargs):
        if self.user:
            #allows the professor change to their own name if they dont like the admin-assigned name
            self.name = self.user.full_name
        super(Professor, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __unicode__(self):
        return self.name


#A session is a lecture or course scheduled for aparticular day/time
class Session(models.Model):
    course = models.ForeignKey(Course, related_name="sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
