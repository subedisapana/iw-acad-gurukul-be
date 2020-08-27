from notice.models import Notice
from rest_framework import serializers, exceptions
from .models import Assignment
from course.models import Course
import cloudinary
import cloudinary.uploader

class AssignmentSerializer(serializers.ModelSerializer):
    resource_url = serializers.CharField(allow_blank=True)
    course_id = serializers.IntegerField()
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'course_id' ,'resource_url',]
    
    def create(self):
        resource_url = self.validated_data['resource_url']

        if resource_url != '':
            result = cloudinary.uploader.upload(self.validated_data['resource_url'], resource_type = "raw")
            resource_url = result['url']
       
        return Assignment.objects.create(
            title =self.validated_data['title'],
            description = self.validated_data['description'],
            due_date = self.validated_data['due_date'],
            course_id = self.validated_data['course_id'],
            resource_url= resource_url,
        )
    
    def update(self, assignment):
        resource_url = assignment.resource_url
        if resource_url != self.validated_data['resource_url']:
            result = cloudinary.uploader.upload(self.validated_data['resource_url'], resource_type = "raw")
            resource_url = result['url']

        assignment.title = self.validated_data['title']
        assignment.description = self.validated_data['description']
        assignment.due_date=self.validated_data['due_date']
        assignment.resource_url = resource_url
        assignment.course_id = self.validated_data['course_id']
        assignment.save()
        return assignment


