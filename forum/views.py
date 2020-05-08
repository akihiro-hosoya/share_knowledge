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

# Create your views here.
def post_search(request):
    foundPost = Post.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        # 除外リスト作成
        exclusion_list = set([' ', '　'])
        q_list = ''
        for i in keyword:
            # 全角半角の空文字が含まれていたら無視
            if i in exclusion_list:
                pass
            else:
                q_list += i
        query = reduce(
            and_, [Q(title__icontains=q) | Q(text__icontains=q) for q in q_list]
        )
        foundPost = post.filter(query)
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'forum/result.html', {'foundPost': foundPost})

class IndexView(TemplateView):
    template_name = "forum/index.html"

class PostListView(ListView):
    model = Post
    template_name = "forum/post_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('account_login')

        category = Category.objects.get(id=self.kwargs['category'])
        post_list = Post.objects.order_by('-id').filter(category=category)

        context = {'post_list': post_list, 'category_name': Category.objects.filter(id=self.kwargs['category'])[0]}
        return render(request, 'forum/post_list.html', context)

    # def get_queryset(self):
    #     category = Category.objects.get(id=self.kwargs['category'])
    #     queryset = Post.objects.order_by('-id').filter(category=category)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category_key'] = self.kwargs['category']
    #     context['category_name'] = Category.objects.filter(id=self.kwargs['category'])[0]
    #     return context

class CreatePostView(CreateView):
    template_name = "forum/post_form.html"
    redirect_field_name = 'forum/post_confirm.html'
    form_class = PostForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grandcategory_list'] = GrandCategory.objects.all()
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context

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

