from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Comments


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
