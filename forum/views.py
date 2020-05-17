from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from forum.models import Post, NewsPost, Comment, GrandCategory, ParentCategory, Category
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView)
from forum.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from functools import reduce
from operator import and_
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TosView(TemplateView):
    template_name = 'forum/tos.html'
class PrivacyPolicyView(TemplateView):
    template_name = 'forum/privacy_policy.html'
class ContactView(TemplateView):
    template_name = 'forum/contact.html'

class ResultView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'forum/result.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i
            query = reduce(
                        and_, [Q(title__icontains=q) | Q(text__icontains=q) for q in q_list]
                    )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "forum/index.html"
    login_url = '/accounts/login/'

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "forum/post_list.html"

    def get_queryset(self):
        category = Category.objects.get(id=self.kwargs['category'])
        queryset = Post.objects.order_by('-id').filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        context['category_name'] = Category.objects.filter(id=self.kwargs['category'])[0]
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "forum/post_form.html"
    redirect_field_name = 'forum/post_confirm.html'
    form_class = PostForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grandcategory_list'] = GrandCategory.objects.all()
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "forum/post_detail.html"

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "forum/post_draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "forum/post_form.html"
    redirect_field_name = 'forum/post_detail.html'
    form_class = PostForm
    model = Post

class PostConfirmView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "forum/post_confirm.html"

def post_save(request, pk):
    post = get_object_or_404(Post, pk)
    post.save()
    return redirect('post_draft_list', pk=pk)

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'forum/my_posts.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False).order_by('published_date')

class MyAnswersView(LoginRequiredMixin, TemplateView):
    template_name = 'forum/my_answers.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "forum/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

class NewsListView(LoginRequiredMixin, ListView):
    model = NewsPost
    template_name = 'forum/news_list.html'

    def get_queryset(self):
        return NewsPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NewsDetailView(LoginRequiredMixin, DetailView):
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
