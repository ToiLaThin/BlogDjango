from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostCreateForm, PostUpdateForm

# Create your views here.


def HomeView(request):
    return render(request, "blog/index.html")


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    # or id
    ordering = ['-pub_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    #fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
