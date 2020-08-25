from django.db import models
from course.models import Course

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=240)
    description = models.TextField(max_length=240)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to = './uploads', null=True)
    resource_url = models.CharField(max_length=250, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # @property
    # def course(self):
    #     return self.course_set.all()

