from rest_framework import serializers
from .models import Course
from assignment.models import Assignment, AssignmentAnswer
from resources.models import Resource

class AssignmentAnswerSerializer(serializers.ModelSerializer):

    class Meta: 
        model = AssignmentAnswer
        fields = ['id', 'answer', 'user_id', 'remarks']

class AssignmentSerializer(serializers.ModelSerializer):
    assignment_answers = AssignmentAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'resource_url', 'assignment_answers'] 

class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'resource_url', 'posted_at']

class CourseSerializer(serializers.ModelSerializer):
    assignments = AssignmentSerializer(many=True, read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['title', 'assignments', 'resources']
        