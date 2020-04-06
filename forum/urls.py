from django.urls import path
from forum import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
]