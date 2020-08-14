from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gurukul.serializers import UserSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
 
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


class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
        