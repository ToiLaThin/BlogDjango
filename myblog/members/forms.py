from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
# not model form
from django import forms

# ke thua va mo rong UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # neu ko dung model form thi se phai co class Meta
    class Meta:
        model = User
        # password2 la password confirm
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    # bootstrapfy the register form
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# dang le cung phai khai bao __init__() nhu RegisterForm
class ProfileUpdateForm(UserChangeForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=False,
                                 max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False,
                                max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_login = forms.DateTimeField(required=False, disabled=True,
                                     widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    date_joined = forms.DateTimeField(required=False, disabled=True,
                                      widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(required=False,
                                   max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(required=False,
                               max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(required=False,
                                max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    # neu ko dung model form thi se phai co class Meta

    class Meta:
        model = User
        # password2 la password confirm
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active']


class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        # con cach khac xem # 25

    # bootstapify the password change form
    def __init__(self, *args, **kwargs):
        super(PasswordUpdateForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
