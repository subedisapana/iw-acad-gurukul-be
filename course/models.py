from django.db import models
from gurukul.models import UserInfo


class Course(models.Model):
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(UserInfo, null=True, limit_choices_to={'is_staff': True}, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
