from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service
from main.models import Post


class PostGetService(Service):
    post_id = forms.IntegerField()

    def process(self):
        self._check_post_presenсe()
        self.result = self._post
        return self

    @property
    @lru_cache
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def _check_post_presenсe(self):
        if not self._post:
            self.errors["post_id"] = ObjectDoesNotExist(f"Post id {self._post} not found")
