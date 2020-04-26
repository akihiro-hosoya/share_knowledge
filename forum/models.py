from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class GrandCategory(models.Model):
    name = models.CharField('大カテゴリー', max_length=50)

    def __str__(self):
        return self.name

class ParentCategory(models.Model):
    name = models.CharField('中カテゴリー', max_length=50)
    grand = models.ForeignKey(GrandCategory, verbose_name='大カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('小カテゴリー', max_length=50)
    parent = models.ForeignKey(ParentCategory, verbose_name='中カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_confirm", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def approved_comment(self):
        return self.comments.filter(approved_comment=True)

class NewsPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('forum.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

