from django.db import models
from main.models import Post, CustomUser


class Comment(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, verbose_name='Название поста')
    text = models.TextField("")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='parent_%(class)s', verbose_name='Родительский комментарий')



    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)




