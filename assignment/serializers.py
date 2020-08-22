from notice.models import Notice
from rest_framework import serializers, exceptions


class AssignmentSerializer(serializers.ModelSerializer):
    #CourseSerializer
    course = CourseSerializer()
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'description', 'course', 'due_date']

        def save(self):
            new_assignment = Assignment(
                title =self.validated_data['title'],
                content = self.validated_data['content'],
                description = self.validated_data['description'],
                course = self.validated_data['course'],
                due_date = self.validated_data['due_date'],
            )

            new_assignment.save()

            return new_assignment
 