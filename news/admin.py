from django.contrib import admin
from news.models import News, Comments


class CommentsInline(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    search_fields = ['title']
    inlines = [CommentsInline]
    fieldsets = (
        ('Название и содержание', {
            'fields': ('title', 'content')
        }),
        ('Архив', {
            'fields': ('archive_status',)
        })
    )


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'pub_date']
    search_fields = ['user_name']
    list_filter = ['user_name']
    fieldsets = (
        ('Новость', {
            'fields': ('news',)
        }),
        ('Данные о комментарии', {
            'fields': ('user_name', 'comment')
        })
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
