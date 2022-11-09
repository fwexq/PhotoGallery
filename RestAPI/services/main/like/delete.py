from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from RestAPI.errors import ForbiddenError
from main.models import CustomUser, Post, Like


class DeleteLikeService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()

    def process(self):
        if self._post:
            self._check_user_rights()
            if self.errors:
                return self
            else:
                self._delete_post()
                self.result = self._post

        return self

    @property
    @lru_cache
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data["post_id"])
        except ObjectDoesNotExist:
            return None

    @property
    @lru_cache()
    def _like(self):
        try:
            return Like.objects.get(user=self.cleaned_data['user'], post=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def _delete_post(self):
        self._post.delete()


    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._like.user_id:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} has no rights")


