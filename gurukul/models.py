from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail



class UserInfo(AbstractUser):
    username = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    profile_image_url = models.CharField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True)
    email = models.EmailField(max_length=240, unique=True)
    bio = models.TextField(null= True, blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    # groups = None
    # user_permissions = None

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for your password",
        # message:
        email_plaintext_message,
        # from:
        "noreply@gurukulhost.local",
        # to:
        [reset_password_token.user.email]
    )

class InstructorRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=30)
    resume = models.FileField(upload_to='gurukul/instructor_request/', null=True)
    resume_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
       return self.full_name
       