from notice.models import Notice
from rest_framework import serializers, exceptions
from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    #CourseSerializer
    # course = CourseSerializer()
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'content', 'description', 'course', 'due_date', 'resources']

        def save(self):
            new_assignment = Assignment(
                title =self.validated_data['title'],
                content = self.validated_data['content'],
                description = self.validated_data['description'],
                course_id = self.validated_data['course'],
                due_date = self.validated_data['due_date'],
            )

            result = cloudinary.uploader.upload(file, 
                            resource_type = "video")
            new_assignment.resource_url = result['url']

            new_assignment.save()
            return new_assignment

       
    