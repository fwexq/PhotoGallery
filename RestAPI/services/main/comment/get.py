from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service
from main.models import Comment


class CommentDetailService(Service):
    post_id = forms.IntegerField()

    def process(self):
        self._check_comment_presence()
        self.result = self._comment
        return self

    @property
    @lru_cache
    def _comment(self):
        try:
            return Comment.objects.get(pk=self.cleaned_data["post_id"])
        except ObjectDoesNotExist:
            return None

    def _check_comment_presence(self):
        if not self._comment:
            self.errors["post_id"] = ObjectDoesNotExist(f"Comment id {self._post} not found")