from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service

from main.models import Post


class PostListService(Service):
    title = forms.CharField(required=False, max_length=40)
    description = forms.CharField(required=False, max_length=80)
    photo = forms.CharField(required=False)

    def process(self):
        self._check_posts_presence()
        self.result = self._posts
        return self


    @property
    @lru_cache
    def _posts(self):
        try:
            return Post.objects.all()
        except ObjectDoesNotExist:
            return None

    def _check_posts_presence(self):
        if not self._posts:
            self.errors["pk"] = ObjectDoesNotExist("Posts not found")


