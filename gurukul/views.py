from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gurukul.serializers import UserSerializer, LoginSerializer, PasswordResetRequestSerializer
from rest_framework.views import APIView
from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import UserInfo
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from .utils import Util

 
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


class PasswordResetRequest(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']

        if UserInfo.objects.filter(email=email).exists():
            user = UserInfo.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user) #for unique token
            current_site = get_current_site(
                request= request).domain
            relative_link = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relative_link
            email_body = 'Hello, \n Use the link below to reset the password \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your password'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        pass




