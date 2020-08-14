from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gurukul.serializers import UserSerializer
from rest_framework.views import APIView
 
class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            new_account = serializer.save()
            data['response'] = "user registered successfully"
            data['email'] = new_account.email
            data['first_name'] = new_account.first_name
            data['middle_name'] = new_account.middle_name
            data['last_name'] = new_account.last_name
            data['profile_image_url'] = new_account.profile_image_url
            return Response(data)

        return Response(serializer.errors)
