from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from .forms import PostCreateForm, PostUpdateForm
from django.http import HttpResponseRedirect

# Create your views here.


def HomeView(request):
    return render(request, "blog/index.html")


# chi co classView này mới có category menu (nếu có category menu context thì hiển thị dropdown)
# nên những template khác sẽ không có dropdown thay vào đó là link
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    # or id
    ordering = ['-pub_date']

    # hàm này sẽ gọi lấy context của các lớp cha của lớp PostListView và thêm vào context category_list
    # các context được đưa vào template sẽ là kq của hàm này. Đây là cách pass context vô generic view
    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['category_list'] = category_list
        return context


def CategoryListView(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list,
    }
    template_name = 'blog/category_list.html'
    return render(request, template_name, context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):        
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        liked = None
        selected_post = get_object_or_404(Post, id=self.kwargs['pk'])
        #xem da like bai do hay chua
        if selected_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        else: 
            liked = False

        context['liked'] = liked
        context['total_likes'] = selected_post.likes_count()
        return context

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


def PostList_CategoryView(request, category_selected: str):
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


def LikePostView(request, pk):
    liked_post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = None  # user already liked this post or not
    # xem lai id user hien tai
    if liked_post.likes.filter(id=request.user.id).exists():
        liked_post.likes.remove(request.user)
        liked = False
    else:
        liked_post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    # ko co template name ma chi quay lai dung trang do
