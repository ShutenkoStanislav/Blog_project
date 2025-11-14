from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    publish_date = models.DateTimeField()
    def __str__(self):
        return self.title



# Створення представлення для відображення постів
# Створіть представлення у файлі views.py, яке витягує всі пости з бази даних і передає їх до шаблону.
