from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', HomeView, name='home'),
    path('posts', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

]
