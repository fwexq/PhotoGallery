from functools import lru_cache
from main.tasks import delete_post_over_time
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from RestAPI.errors import ForbiddenError
from main.models import CustomUser, Post


class PostDeleteService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField(required=True)

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

    def _delete_post(self):
        delete_post_over_time.apply_async((self._post.pk, ), countdown=40)
        # self._post.delete()


    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._post.author.id:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} has no rights")

