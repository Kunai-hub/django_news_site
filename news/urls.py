from django.urls import path

from news.views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, login_user, logout_user, \
    register_user, upload_file

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('users/login/', login_user, name='login_user'),
    path('users/logout/', logout_user, name='logout_user'),
    path('users/register/', register_user, name='register_user'),
    path('files/upload_file/', upload_file, name='upload_file'),
]
