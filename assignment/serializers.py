from notice.models import Notice
from rest_framework import serializers, exceptions
from .models import Assignment, AssignmentAnswer
from course.models import Course
import cloudinary
import cloudinary.uploader
import os

class AssignmentSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'course_id' , 'resource', 'resource_url',]
    
    def save(self):
        assignment_obj = Assignment(
            title =self.validated_data['title'],
            description = self.validated_data['description'],
            due_date = self.validated_data['due_date'],
            course_id = self.validated_data['course_id'],
            resource = self.validated_data['resource'],
        )
        assignment_obj.save()
    
        if assignment_obj.resource != '':
            result = cloudinary.uploader.upload(assignment_obj.resource, resource_type = "raw")
            assignment_obj.resource_url = result['url']
            assignment_obj.save()

        os.remove(assignment_obj.resource.path)

        return assignment_obj
    
    def update(self, assignment):

        if self.validated_data['resource'] != assignment.resource:
            cloudinary.uploader.destroy(assignment.resource_url)
            assignment.resource = self.validated_data['resource']
            assignment.save()
            assignment_upload = cloudinary.uploader.upload(assignment.resource, resource_type = "raw")
            assignment.resource_url = assignment_upload['url']
            assignment.save()
            os.remove(assignment.resource.path)

        assignment.title = self.validated_data['title']
        assignment.description = self.validated_data['description']
        assignment.course_id = self.validated_data['course_id']
        assignment.due_date = self.validated_data['due_date']

        assignment.save()
        
        return assignment
       

class AssignmentAnswerSerializer(serializers.ModelSerializer):
    assignment_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    class Meta:
        model = AssignmentAnswer
        fields = ['id', 'answer', 'assignment_id', 'user_id', 'remarks']
