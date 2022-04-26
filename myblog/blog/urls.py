from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryCreateView,
    PostList_CategoryView,
    CategoryListView,
    LikePostView,
    ChartView,
)

urlpatterns = [
    path('', HomeView, name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('categories/', CategoryListView, name='category_list'),
    path('posts_category/<str:category_selected>/',
         PostList_CategoryView, name='post_list_category'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('posts/<int:pk>/like/', LikePostView, name='like_post'),
    path('statistic', ChartView, name='statistic'),

]
