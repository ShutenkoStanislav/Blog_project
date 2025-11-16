from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    publish_date = models.DateTimeField()
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, related_name="post_author", null=True, blank=True)
    
    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.publish_date <= now

    
    def __str__(self):
        return self.title








