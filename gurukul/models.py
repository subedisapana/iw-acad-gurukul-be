from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    username = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    profile_image_url = models.CharField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True)
    email = models.EmailField(max_length=240, unique=True)
    bio = models.TextField(null= True, blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    groups = None
    user_permissions = None

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.title
    