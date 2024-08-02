from django.shortcuts import render
from django.views import View, generic

from news.models import News
from news.forms import NewsForm


class NewsListView(View):

    def get(self, request):
        news_list = News.objects.all()
        return render(request,
                      'news/news_list.html',
                      {'news_list': news_list})


class NewsDetailView(generic.DetailView):
    model = News
