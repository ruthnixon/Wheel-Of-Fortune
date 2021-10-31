from django.db import models
import datetime

# Create your models here.
### The code below creates a post object to be used in my database.

class Post(models.Model):
    title=models.CharField(max_length=30)
    body=models.CharField(max_length=500)
    date_posted=datetime.datetime.now()
    

