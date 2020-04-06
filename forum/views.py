from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = "forum/index.html"

class PostListView(TemplateView):
    template_name = "forum/post_list.html"