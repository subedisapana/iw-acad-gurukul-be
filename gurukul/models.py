from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    username = None
    middle_name = models.CharField(max_length=30, blank=True)
    profile_image_url = models.CharField(max_length=250, null=True)
    profile_image = models.ImageField(upload_to='profile_image/')
    email = models.EmailField(max_length=240, unique=True)
    bio = models.TextField(null= True )
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    groups = None
    user_permissions = None

