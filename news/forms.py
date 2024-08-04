from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Ваше имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Ваша фамилия')
    email = forms.EmailField(required=False, help_text='Ваша электронная почта')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
