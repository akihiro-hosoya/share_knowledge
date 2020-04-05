from django.conf import settings
from django.db import models
from django.contrib import admin
from django.urls import reverse


# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.save()

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={'pk':self.pk})

	def __str__(self):
		return self.title