import datetime

from django.utils import timezone

from compet.celery import app
from main.models import Post


@app.task
def delete_post_over_time(self):
    post = Post.objects.get(pk=self)
    return post.delete()



