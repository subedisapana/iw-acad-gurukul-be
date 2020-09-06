from django.http import Http404
from gurukul.serializers import UserSerializer, LoginSerializer, UserUpdateSerializer, ChangePasswordSerializer, InstructorRequestSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from .models import UserInfo, InstructorRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        current_user = self.get_object(pk)
        user_data = {}
        user_data['id'] = current_user.id
        user_data['email'] = current_user.email
        user_data['first_name'] = current_user.first_name
        user_data['middle_name'] = current_user.middle_name
        user_data['last_name'] = current_user.last_name
        user_data['bio'] = current_user.bio
        user_data['profile_image_url'] = current_user.profile_image_url

        return Response(user_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        current_user = self.get_object(pk)
        serializer = UserUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            updated_account = serializer.update(current_user)
            data = {}

            data['id'] = updated_account.id
            data['email'] = updated_account.email
            data['first_name'] = updated_account.first_name
            data['middle_name'] = updated_account.middle_name
            data['last_name'] = updated_account.last_name
            data['bio'] = updated_account.bio
            data['profile_image_url'] = updated_account.profile_image_url
            
            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        current_user = self.get_object(pk)
        current_user.delete()
        return Response('user deleted', status=status.HTTP_204_NO_CONTENT)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            new_account = serializer.save()
            data['response'] = "user registered successfully"
            data['id'] = new_account.id
            data['email'] = new_account.email
            data['first_name'] = new_account.first_name
            data['middle_name'] = new_account.middle_name
            data['last_name'] = new_account.last_name
            data['profile_image_url'] = new_account.profile_image_url
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id, "is_staff": user.is_staff }, status=200)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserInfo
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorRequestView(APIView):

    def post(self, request):
        serializer = InstructorRequestSerializer(data = request.data)
        if serializer.is_valid():
            new_request = serializer.save()
            data = {}
            data['id'] = new_request.id
            data['full_name'] = new_request.full_name
            data['address'] = new_request.address
            data['resume_url'] = new_request.resume_url
            data['phone_number'] = new_request.phone_number

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    