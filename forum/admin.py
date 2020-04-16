from django.contrib import admin
from .models import Post, NewsPost, Comment, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(NewsPost)
admin.site.register(Comment)
admin.site.register(Category)
