from django.shortcuts import render
from rest_framework.views import APIView
from assignment.serializers import AssignmentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Assignment
from django.http import Http404


# Create your views here.
class AssignmentView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Assignment.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = AssignmentSerializer(data = request.data)

        if serializer.is_valid():
            new_assignment = serializer.create()
            data = {}

            data['id'] = new_assignment.id
            data['title'] = new_assignment.title
            data['description'] = new_assignment.description
            data['due_date'] = new_assignment.due_date
            data['resource_url'] = new_assignment.resource_url

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        assignment = self.get_object(pk)
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            updated_assignment = serializer.update(assignment)

            updated_data = {}

            updated_data['id'] = updated_assignment.id
            updated_data['title'] = updated_assignment.title
            updated_data['description'] = updated_assignment.description
            updated_data['due_date'] = updated_assignment.due_date
            updated_data['resource_url'] = updated_assignment.resource_url
            
            return Response(updated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assignment  = self.get_object(pk)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
