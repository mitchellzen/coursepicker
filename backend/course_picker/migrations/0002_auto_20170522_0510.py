# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_picker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='professors',
        ),
        migrations.AddField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(null=True, related_name='professors', to='course_picker.Course'),
        ),
    ]
