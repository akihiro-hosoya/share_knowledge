from django.urls import path
from forum import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/confirm/', views.PostConfirmView.as_view(), name='post_confirm'),
    path('post/profile/', views.ProfileListView.as_view(), name='profile'),
    path('myposts/', views.MyPostsView.as_view(), name='my_posts'),
    path('myanswers/', views.MyAnswersView.as_view(), name='my_answers'),    
]