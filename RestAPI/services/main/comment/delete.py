from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import CustomUser, Comment


class DeleteCommentService(Service):
    post_id = forms.IntegerField()
    user = ModelField(CustomUser)

    def process(self):
        if self._comment:
            self._check_user_rights()
            self._delete_post()
            self.result = self._comment
        return self
    @property
    @lru_cache
    def _comment(self):
        try:
            return Comment.objects.get(pk=self.cleaned_data["post_id"])
        except ObjectDoesNotExist:
            return None

    def _delete_post(self):
        self._comment.delete()

    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._comment.user_id:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} has no rights")
        else:
            pass

