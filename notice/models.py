from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def published_day(self):
        return self.created_at.strftime('%B %d, %Y')
