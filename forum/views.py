from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from forum.models import Post, NewsPost, Comment
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView)
from forum.forms import PostForm, CommentForm
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
    redirect_field_name = 'forum/post_confirm.html'
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

class PostConfirmView(DetailView):
    model = Post
    template_name = "forum/post_confirm.html"

def post_save(request, pk):
    post = get_object_or_404(Post, pk)
    post.save()
    return redirect('post_draft_list', pk=pk)

class ProfileListView(TemplateView):
    template_name = 'forum/profile.html'

class MyPostsView(ListView):
    model = Post
    template_name = 'forum/my_posts.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False).order_by('published_date')

class MyAnswersView(TemplateView):
    template_name = 'forum/my_answers.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = "forum/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

class NewsListView(ListView):
    model = NewsPost
    template_name = 'forum/news_list.html'

    def get_queryset(self):
        return NewsPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NewsDetailView(DetailView):
    model = NewsPost
    template_name = "forum/news_detail.html"

def post_comment(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'forum/post_comment.html', {'form': form})
