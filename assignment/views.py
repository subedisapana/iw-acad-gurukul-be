from django.shortcuts import render
from rest_framework.views import APIView
from assignment.serializers import AssignmentSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class AssignmentView(APIView):
    def post(self, request):
        serializer = AssignmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        assignment = self.get_object(pk)
        serializer = AssignmentSerializer(assignment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assignment  = self.get_object(pk)
        assignment .delete()
        return Response(status=status.HTTP_204_NO_CONTENT)