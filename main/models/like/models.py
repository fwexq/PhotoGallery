from django.db import models


class Like(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return str(self.post)



    class Meta:
        db_table = 'likes'
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
