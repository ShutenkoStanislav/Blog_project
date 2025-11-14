from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    publish_date = models.DateTimeField()



# У додатку blog, створіть модель Post з полями:

#  title (CharField),
#  content (TextField), та 
# published_date (DateTimeField).
# За бажанням ви можете додати власні поля. 
