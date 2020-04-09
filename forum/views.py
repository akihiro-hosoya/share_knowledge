from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from forum.models import Post
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView)
from forum.forms import PostForm
from django.utils import timezone


# Create your views here.
class IndexView(TemplateView):
    template_name = "forum/index.html"

class PostListView(ListView):
    model = Post
    template_name = "forum/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class CreatePostView(CreateView):
    template_name = "forum/post_form.html"
    redirect_field_name = 'forum/post_detail.html'
    form_class = PostForm
    model = Post

class PostDetailView(DetailView):
    model = Post
    template_name = "forum/post_detail.html"

class DraftListView(ListView):
    model = Post
    template_name = "forum/post_draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

class PostUpdateView(UpdateView):
    template_name = "forum/post_form.html"
    redirect_field_name = 'forum/post_detail.html'
    form_class = PostForm
    model = Post
