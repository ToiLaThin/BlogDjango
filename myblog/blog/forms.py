from random import choice
from django import forms
from .models import Post, Category

# tra ve queryset
# doan code nay chỉ chạy khi restart server/save file này lại
choices = Category.objects.all().values_list('name', 'name')
choice_lst = []
for choice in choices:
    choice_lst.append(choice)


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author',
                  'body', 'pub_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your blog title into here!!!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_lst, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # dung widget cho field nay la DateInput
            'pub_date': forms.DateInput(attrs={'class': 'form_control'}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_lst, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
