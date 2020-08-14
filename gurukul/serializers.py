from rest_framework import serializers
from gurukul.models import UserInfo
import cloudinary
import cloudinary.uploader
import os

#User Serializer
class UserSerializer(serializers.ModelSerializer): 

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserInfo
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only': True}
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
