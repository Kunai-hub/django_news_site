from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Comments, Profile
from .forms import AuthForm, RegisterForm, UploadFileForm


class NewsListView(View):

    def get(self, request):
        news_list = News.objects.all()
        return render(request,
                      'news/news_list.html',
                      {'news_list': news_list})


class NewsDetailView(View):

    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        comments = Comments.objects.filter(news=news)
        return render(request,
                      'news/news_detail.html',
                      {'news': news, 'comments': comments})

    def post(self, request, pk):
        news = News.objects.get(pk=pk)
        if request.user.is_authenticated:
            author = request.user.username
        else:
            author = request.POST['user_name']
        comment = request.POST['comment']
        Comments.objects.create(news=news, user_name=author, comment=comment)
        return redirect('news_detail', pk=pk)


class NewsCreateView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request,
                      'news/news_create.html')

    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        new_news = News.objects.create(title=title, content=content)
        return redirect('news_list')


class NewsUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        return render(request,
                      'news/news_update.html',
                      {'news': news})

    def post(self, request, pk):
        title = request.POST['title']
        content = request.POST['content']
        news = News.objects.get(pk=pk)
        news.title = title
        news.content = content
        news.edit_date = timezone.now()
        news.save()
        return redirect('news_list')


def login_user(request):
    now = datetime.now()
    hour_now = now.hour

    if request.method == 'POST':
        user_form = AuthForm(request.POST)

        if 8 < hour_now < 22:

            if user_form.is_valid():
                username = user_form.cleaned_data['username']
                password = user_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user:

                    if user.is_active:

                        if user.is_superuser:
                            user_form.add_error('__all__', 'Ошибка! Запрещен вход администраторам!')
                        else:
                            login(request, user)
                            return HttpResponse('Вы успешно вошли в систему!')
                    else:
                        user_form.add_error('__all__', 'Ошибка! Пользователь неактивен!')
                else:
                    user_form.add_error('__all__', 'Ошибка! Проверьте правильность логина или пароля!')
        else:
            user_form.add_error('__all__', 'Ошибка! Запрещен вход на сайт с 22:00 до 08:00')
    else:
        user_form = AuthForm()

    context = {
        'form': user_form
    }

    return render(request,
                  'news/login_user.html',
                  context=context
                  )


def logout_user(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из учетной записи!')


def register_user(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            birthday = form.cleaned_data.get('birthday')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(
                user=user,
                birthday=birthday,
                city=city,
                phone=phone
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,
                  'news/register_user.html',
                  context={'form': form})


def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']
            stopwords = ['cat', 'dog']
            filedata = file.read()
            if any(word.encode('utf-8') in filedata for word in stopwords):
                return HttpResponse('Ошибка! Файл не прошёл проверку!')
            else:
                return HttpResponse(content=file.name, status=200)
    else:
        form = UploadFileForm()
    return render(request,
                  'news/upload_file.html',
                  context={'form': form})
