from resources.models import Resources
from rest_framework import serializers, exceptions
import cloudinary
import cloudinary.uploader
import os


class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['id', 'title', 'content','resource_url','course_ic']

        def save(self):
            new_resource = Resources(
                title =self.validated_data['title'],
                content = self.validated_data['content'],
                resource_url =self.validated_data['resource_url'],
                course_id=self.validated_data['course']
            )

            if resource_url!= "":
                uploader=cloudinary.uploader.upload(os.path.abspath("./resources/resource"))
                new_resource.resource_url=uploader['url']

            new_resource.save()

            return new_resource
