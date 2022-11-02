from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post, Comment


class CommentCreateService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()
    text = forms.CharField()
    parent = forms.IntegerField(required=False)

    def process(self):
        self._check_post_presenсe()
        if self._post:
            self._create_comment()
            self.result = self._create_comment()
        return self

    @property
    @lru_cache
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def _create_comment(self):
        comment = Comment(
            text=self.cleaned_data['text'],
            user=self.cleaned_data['user'],
            post_id=self.cleaned_data['post_id']
        )
        if self.cleaned_data['parent']:
            comment.parent_id = self.cleaned_data['parent']
        comment.save()
        return comment

    def _check_post_presenсe(self):
        if not self._post:
            self.errors["pk"] = ObjectDoesNotExist(f"Post id {self._post} not found")
