from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Course
from .serializer import CourseSerializer
from django.http import Http404, HttpResponse
from gurukul.models import UserInfo
from django.core import serializers
 
class CourseView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
 
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

class UserCourseView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    
    
    def get(self, request, user_id, format=None):
        user_courses = Course.objects.filter(users__id=user_id)
        data = serializers.serialize('json', user_courses)
        
        return HttpResponse(data, content_type="application/json") 
