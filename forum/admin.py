from django.contrib import admin
from .models import Category, Post, NewsPost,Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(NewsPost)
admin.site.register(Comment)
