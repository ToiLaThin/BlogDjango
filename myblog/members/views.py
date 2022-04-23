from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
# dango PasswordChangeView
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm, ProfileUpdateForm, PasswordUpdateForm

# Create your views here.


class UserCreateView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('post_list')

    def get_object(self):
        return self.request.user


class PasswordUpdateView(PasswordChangeView):
    # we can specify template_name in urls.py inside the view call
    #template_name = 'registration/password_update.html'
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('post_list')
