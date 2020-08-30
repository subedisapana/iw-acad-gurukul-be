from django.db import models
from gurukul.models import UserInfo


class Course(models.Model):
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(UserInfo)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
