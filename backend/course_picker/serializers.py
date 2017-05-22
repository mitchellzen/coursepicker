from django.contrib.auth.models import User
from rest_framework import serializers
from course_picker.models import Course, Professor, Session


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    #todo https://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/ to create users
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('name',)


class SessionSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    class Meta:
        model = Session
        fields = ('start_time','end_time')



class CourseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    cost = serializers.DecimalField(max_digits=10,decimal_places=2)
    description = serializers.CharField(required=False, allow_blank=True)
    professors = ProfessorSerializer(many=True, read_only=True)
    #serializers.HyperlinkedRelatedField(view_name='professor-detail', lookup_field='courses', read_only=True, many=True)
    sessions = SessionSerializer(many=True, read_only=True)
    #serializers.HyperlinkedRelatedField(view_name='session-detail', lookup_field='sessions', read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'
