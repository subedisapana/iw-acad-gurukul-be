from rest_framework import serializers
from .models import Course
from assignment.models import Assignment
from resources.models import Resource

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'resource_url'] 

class ResoruceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'resource_url', 'posted_at']

class CourseSerializer(serializers.ModelSerializer):
    assignments = AssignmentSerializer(many=True, read_only=True)
    resources = ResoruceSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['title', 'assignments', 'resources']
