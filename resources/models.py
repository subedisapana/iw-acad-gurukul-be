from django.db import models
from course.models import Course

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.FileField(upload_to='resources/resource/', blank=True)
    resource_url = models.CharField(max_length=500,blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = 'resources')

    def __str__(self):
        return self.title
