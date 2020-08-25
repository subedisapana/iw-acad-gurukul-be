from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from resources.models import Resources
from resources.serializers import ResourcesSerializer
 
# Create your views here.

class ResourcesView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        resources = Resources.objects.all()
        serializer = ResourcesSerializer(resources, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ResourcesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        Resource = self.get_object(pk)
        serializer = ResourcesSerializer(Resource, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Resources = self.get_object(pk)
        Resources.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
