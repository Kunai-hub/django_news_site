from datetime import timezone

from django.db import models


class News(models.Model):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive')
    ]
    title = models.CharField(max_length=25, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    edit_date = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=1, choices=STATUS_CHOICES, default='a')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']


class Comments(models.Model):
    user_name = models.CharField(max_length=25, verbose_name='Имя пользователя')
    comment = models.TextField(verbose_name='Комментарий')
    pub_date = models.DateTimeField(verbose_name='Дата комментария', auto_now_add=True)
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Новость')

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['pub_date']
