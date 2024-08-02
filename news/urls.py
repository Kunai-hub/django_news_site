from django.urls import path

from news.views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
]
