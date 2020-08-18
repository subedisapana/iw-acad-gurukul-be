from django.db import models
from gurukul.models import UserInfo


class Course(models.Model):
    title = models.CharField(max_length=50)
    user = models.ManyToManyField(UserInfo, limit_choices_to={'is_staff': True})

    def __str__(self):
        return self.title
