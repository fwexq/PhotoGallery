from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Like, Post


class LikeService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()

    def process(self):
        self.check_post_presence()
        self.check_like_presence()
        if self.errors:
            return self
        if self._post:
            if self._check_status_post():
                self.result = Like.objects.create(user=self.cleaned_data['user'], post=self._post)
        return self

    @property
    @lru_cache()
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def check_post_presence(self):
        if not self._post:
            self.errors['pk'] = f"Post id {self.cleaned_data['post_id']} does not exist"


    @property
    @lru_cache()
    def _like(self):
        try:
            return Like.objects.get(user=self.cleaned_data['user'], post=self.cleaned_data['post_id'])
        except ObjectDoesNotExist:
            return None

    def check_like_presence(self):
        if self._like:
            self.errors['like'] = f"You have already liked the post id {self.cleaned_data['post_id']}"
        else:
            pass

    def _check_status_post(self):
        if self._post.moderation_status == 'VALID':
            return self._post
        else:
            self.errors['moderation_status'] = "Status must be VALID"




        # self.like = Like(
        #     user=self.cleaned_data['user'],
        #     pk=self.cleaned_data['post_id']
        # )
        # if self.cleaned_data['user'] in self._post.likes.all():
        #     self._post.likes.remove(self.cleaned_data['user'])
        # else:
        #     self._post.likes.add(self.cleaned_data['user'])
        #     is_likes = True
        # self._post.save()
        # outcome = is_likes
        # return outcome
