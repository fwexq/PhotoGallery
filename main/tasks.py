from celery import shared_task
from compet.celery import app
from main.models import Post


@shared_task()
def delete_post_over_time(post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return "good"

