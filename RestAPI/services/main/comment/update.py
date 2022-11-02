from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import Comment


class CommentUpdateService(Service):
    post_id = forms.IntegerField()
    text = forms.CharField(required=True, max_length=255)

    def process(self):
        self._check_comment_presence()
        if self._comment:
            self._check_user_rights()
            self._update_comment()
            self.result = self._comment
        return self

    @property
    @lru_cache
    def _comment(self):
        try:
            return Comment.objects.get(pk=self.cleaned_data["post_id"])
        except ObjectDoesNotExist:
            return None

    def _update_comment(self):
        if self.cleaned_data['text']:
            self._comment.text = self.cleaned_data['text']
        self._comment.save()

    def _check_user_rights(self):
        if not self.data["user"].id == self._comment.user_id:
            self.errors["user"] = ForbiddenError(f"User id {self.data['user'].id} has no rights")

    def _check_comment_presence(self):
        if not self._comment:
            self.errors["post_id"] = ObjectDoesNotExist(f"Comment pk {self._comment} does not exist")
        else:
            pass

