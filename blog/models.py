from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автора"
        ordering = ["name"]

    
    
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
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ["-publish_date"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField()
    def __str__(self):
        return f"{self.author_name} - {self.post}"
    
    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ["-created_date"]









