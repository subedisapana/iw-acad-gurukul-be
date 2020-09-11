from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from resources.models import Resource
from resources.serializer import ResourceSerializer
 
# Create your views here.

class ResourceView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ResourceSerializer(data=request.data)

        if serializer.is_valid():
            new_resource = serializer.save()
            resource_abs_path = new_resource.content.path
            resource_rel_path = "/" + resource_abs_path[resource_abs_path.find('resources'):]

            data = {}
            data['id'] = new_resource.id
            data['title'] = new_resource.title
            data['description'] = new_resource.description
            data['content'] = resource_rel_path
            data['content_url'] = new_resource.content_url
            data['course_id'] = new_resource.course_id

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(data=request.data)

        if serializer.is_valid():
            updated_resource = serializer.update(resource)

            content_abs_path = updated_resource.content.path
            content_rel_path = content_abs_path[content_abs_path.find('resources'):]
            
            updated_data = {}

            updated_data['id'] = updated_resource.id
            updated_data['title'] = updated_resource.title
            updated_data['description'] = updated_resource.description
            updated_data['course_id'] = updated_resource.course_id
            updated_data['content'] = content_rel_path
            updated_data['content_url'] = updated_resource.content_url
            
            return Response(updated_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        resource = self.get_object(pk)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
