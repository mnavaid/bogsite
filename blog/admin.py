from django.contrib import admin
from .models import BlogPosts
# Register your models here.
@admin.register(BlogPosts)

class PostsMOdelAdmin(admin.ModelAdmin):
  list_display=['id','title','description']