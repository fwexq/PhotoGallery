from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import Post


class PostUpdateService(Service):
    pk = forms.IntegerField()
    title = forms.CharField(required=False, max_length=40)
    description = forms.CharField(required=False, max_length=80)
    photo = forms.ImageField(required=False)

    def process(self):
        self._check_post_presence()
        if self._post:
            if self._check_user_rights():
                self._update_post()
                self.result = self._post
        return self

    @property
    @lru_cache()
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['pk'])
        except ObjectDoesNotExist:
            return None

    def _update_post(self):
        if self.cleaned_data['title']:
            self._post.title = self.cleaned_data['title']
        if self.cleaned_data['description']:
            self._post.description = self.cleaned_data['description']
        if self.cleaned_data['photo']:
            self._post.previous_photo = self._post.photo
            self._post.photo = self.cleaned_data['photo']
        self._post.moderation_status = 'NOT_MODERATED'
        self._post.save()

    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._post.author.id:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} has no rights")

    def _check_post_presence(self):
        if self._post:
            pass
        else:
            self.errors["pk"] = ObjectDoesNotExist(f"Post pk {self.cleaned_data['pk']} not found")


