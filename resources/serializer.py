from resources.models import Resource
from rest_framework import serializers, exceptions
import cloudinary
import cloudinary.uploader
import os


class ResourceSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'content', 'content_url', 'course_id']

    def save(self):
        resource_obj = Resource(
            title =self.validated_data['title'],
            description = self.validated_data['description'],
            course_id=self.validated_data['course_id'],
            content=self.validated_data['content'],
        )
        resource_obj.save()
        
        if resource_obj.content != '':
            result = cloudinary.uploader.upload(resource_obj.content, resource_type = "raw")
            resource_obj.content_url = result['url']
            resource_obj.save()

        os.remove(resource_obj.content.path)

        return resource_obj


    def update(self, resource):
        if self.validated_data['content'] != resource.content:
            cloudinary.uploader.destroy(resource.content_url)
            resource.content = self.validated_data['content']
            resource.save()
            resource_upload = cloudinary.uploader.upload(resource.content, resource_type = "raw")
            resource.content_url = resource_upload['url']
            resource.save()
            os.remove(resource.content.path)

        resource.title = self.validated_data['title']
        resource.description = self.validated_data['description']
        resource.course_id = self.validated_data['course_id']

        resource.save()
        
        return resource