from functools import lru_cache
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service
from main.models import Post


class PostListService(Service):
#просмотр постов текущего пользователя
    def process(self):
        self.result = Post.objects.filter(moderation_status="VALID")
        return self





