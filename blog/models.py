from django.db import models

# Blog Post Model.

class BlogPosts(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField()
  

