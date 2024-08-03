from django.contrib import admin
from news.models import News, Comments


class CommentsInline(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'status']
    actions = ['mark_as_active', 'mark_as_inactive']
    search_fields = ['title']
    list_filter = ['status']
    inlines = [CommentsInline]
    fieldsets = (
        ('Название и содержание', {
            'fields': ('title', 'content')
        }),
        ('Статус', {
            'fields': ('status',)
        })
    )

    def mark_as_active(self, request, queryset):
        queryset.update(status='a')

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='i')

    mark_as_active.short_description = 'Перевести в статус \'Активна\''
    mark_as_inactive.short_description = 'Перевести в статус \'Неактивна\''


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
