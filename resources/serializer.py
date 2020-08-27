from resources.models import Resource
from rest_framework import serializers, exceptions
import cloudinary
import cloudinary.uploader
import os


class ResourceSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description','resource_url','course_id']

    def create(self):
        resource_url = self.validated_data['resource_url']

        if resource_url != '':
            result = cloudinary.uploader.upload(self.validated_data['resource_url'], resource_type = "raw")
            resource_url = result['url']
       
        return Resource.objects.create(
            title =self.validated_data['title'],
            description = self.validated_data['description'],
            course_id=self.validated_data['course_id'],
            resource_url= resource_url,
        )

    def update(self, resource):
        resource_url = resource.resource_url

        if resource_url != self.validated_data['resource_url']:
            uploader=cloudinary.uploader.upload(self.validated_data['resource_url'], resource_type = "raw")
            resource_url=uploader['url']

        resource.title = self.validated_data['title']
        resource.description = self.validated_data['description']
        resource.course_id = self.validated_data['course_id']
        resource.resource_url = resource_url

        resource.save()

        return resource
