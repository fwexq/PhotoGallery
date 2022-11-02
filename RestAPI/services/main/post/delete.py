from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from RestAPI.errors import ForbiddenError
from main.models import CustomUser, Post


class DeletePostService(Service):
    post_id = forms.IntegerField()
    user = ModelField(CustomUser)

    def process(self):
        # self.check_post_presence()
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
        self._post.delete()


    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._post.author.id:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} has no rights")

    # def check_post_presence(self):
    #     if not self._post:
    #         self.errors["pk"] = ObjectDoesNotExist(f"Post pk {self.cleaned_data['pk']} not found")
