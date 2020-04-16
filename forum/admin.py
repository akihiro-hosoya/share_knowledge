from django.contrib import admin
from .models import Post, NewsPost, Comment, Camera

# Register your models here.
admin.site.register(Post)
admin.site.register(NewsPost)
admin.site.register(Comment)
admin.site.register(Camera)
