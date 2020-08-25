from django.db import models
from course.models import Course

# Create your models here.
class Resources(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='resources/resource/')
    resource_url=models.CharField(max_length=500,blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def published_day(self):
        return self.posted_at.strftime('%B %d, %Y')