from django.urls import path
from .views import UserCreateView, UserUpdateView, PasswordUpdateView
# django PasswordChangeView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='register'),
    path('profile/update', UserUpdateView.as_view(), name='profile_update'),
    #path('password/', PasswordChangeView.as_view(template_name='registration/password_update.html')),
    # class view tu define
    path('password/', PasswordUpdateView.as_view(
        template_name='registration/password_update.html'), name='password_update'),
]
