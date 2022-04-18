from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
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


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'blog/category_create.html'
    fields = ['name']


def PostList_CategoryView(request, category_selected):
    # process the slugified category name
    category_selected = category_selected.title().replace('-', ' ')

    posts = Post.objects.filter(
        category=category_selected).order_by('-pub_date')
    context = {
        'posts': posts,
        'category_selected': category_selected,
    }
    template_name = 'blog/post_list_category.html'
    return render(request, template_name, context)
