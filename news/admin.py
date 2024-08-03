from django.contrib import admin
from news.models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


admin.site.register(News, NewsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'pub_date']


admin.site.register(Comments, CommentsAdmin)
