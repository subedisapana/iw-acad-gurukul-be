from rest_framework import serializers, exceptions
from gurukul.models import UserInfo, InstructorRequest
import cloudinary
import cloudinary.uploader
import os
from django.contrib.auth import authenticate


#User Registration
class UserSerializer(serializers.ModelSerializer): 

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = UserInfo
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password', 'confirm_password', 'profile_image_url', 'bio']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        new_account = UserInfo(
                email = self.validated_data['email'],
                first_name = self.validated_data['first_name'],
                middle_name = self.validated_data['middle_name'],
                last_name = self.validated_data['last_name']
            )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Please enter same password'})
        new_account.set_password(password)

        uploader = cloudinary.uploader.upload(os.path.abspath("gurukul/static/img/default-profile.png"), quality="60")
        new_account.profile_image_url = uploader['url']

        new_account.save()
        return new_account
           
class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    middle_name = serializers.CharField(max_length=100, allow_blank=True)
    last_name = serializers.CharField(max_length=100)
    bio = serializers.CharField(max_length=300, allow_blank=True)
    profile_image_url = serializers.CharField(max_length=300)

    def update(self, user):
        profile_image_url = user.profile_image_url

        if profile_image_url != self.validated_data['profile_image_url']:
            uploader = cloudinary.uploader.upload(profile_image_url, quality="60")
            profile_image_url = uploader['url']

        user.email = self.validated_data['email']
        user.first_name = self.validated_data['first_name']
        user.middle_name = self.validated_data['middle_name']
        user.last_name = self.validated_data['last_name']
        user.bio = self.validated_data['bio']
        
        user.profile_image_url = profile_image_url

        user.save()
        
        return user


#User Login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        print(email, password,'***************')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise exceptions.ValidationError("User is not active")
            else:
                raise exceptions.ValidationError("Credentials did not match")
        else:
            raise exceptions.ValidationError("Email and password is required to login")
        
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = UserInfo

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class InstructorRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InstructorRequest
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'resume_url']

    def save(self):
        resume_url = self.validated_data['resume_url']

        if resume_url != '':
            result = cloudinary.uploader.upload(self.validated_data['resume_url'], resource_type = "raw")
            resume_url = result['url']
       
        return InstructorRequest.objects.create(
            full_name =self.validated_data['full_name'],
            email= self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            address=self.validated_data['address'],
            resume_url= resume_url,
        )
