from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post, Like


class LikesService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()

    def process(self):
        self._check_post_presence()
        if self._post:
            self._set_like()
            self.result = self._post
        return self

    @property
    @lru_cache()
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def _check_post_presence(self):
        if self._post:
            pass
        else:
            self.errors["post_id"] = ObjectDoesNotExist(f"Post pk {self.cleaned_data['post_id']} not found")
    def _set_like(self):
        self.like = Like(
            user=self.cleaned_data['user'],
            pk=self.cleaned_data['post_id']
        )
        if self.cleaned_data['user'] in self._post.likes.all():
            self._post.likes.remove(self.cleaned_data['user'])
        else:
            self._post.likes.add(self.cleaned_data['user'])
            is_likes = True
        self._post.save()
        outcome = is_likes
        return outcome