from django.contrib import admin
from news.models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    search_fields = ['title']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'pub_date']
    search_fields = ['user_name']


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
