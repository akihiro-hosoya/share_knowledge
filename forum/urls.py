from django.urls import path
from forum import views

app_name= 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('category/<int:category>', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/confirm/', views.PostConfirmView.as_view(), name='post_confirm'),
    path('myposts/', views.MyPostsView.as_view(), name='my_post_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('news/top/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('post/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('result/', views.ResultView.as_view(), name='result'),
    # 固定ページ
    path('tos/', views.TosView.as_view(), name='tos'),
    path('privacy_policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('contact_complete/', views.contact_complete, name='contact_complete'),
]