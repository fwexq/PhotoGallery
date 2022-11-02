from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import Post, CustomUser


class PostUpdateService(Service):
    post_id = forms.IntegerField()
    title = forms.CharField(required=False, max_length=40)
    description = forms.CharField(required=False, max_length=80)
    photo = forms.ImageField(required=False)
    moderation_status = forms.CharField(required=False)

    def process(self):
        self._check_post_presence()
        if self._post:
            self._check_user_rights()
            self._update_post()
            if self._check_user_role():
                post = self._update_moderation_status()
                self.result = post
            else:
                self.result = self._post
        return self

    @property
    @lru_cache()
    def _post(self):
        try:
            return Post.objects.get(pk=self.cleaned_data['post_id'])
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

    def _update_moderation_status(self):
        moderation_status = self.cleaned_data.get('moderation_status')
        if moderation_status == 'VALID' or moderation_status == "INVALID" or moderation_status == "NOT_MODERATED":
            self._post.moderation_status = moderation_status
            self._post.save()
            return self._post
        else:
            self.errors["moderation_status"] = SyntaxError("There is no such status. Select one of the statuses 'VALID', 'INVALID', 'NOT_MODERATED'")
        return self

    def _check_user_rights(self):
        if not self.data['user'].id == self._post.author.id:
            self.errors["user"] = ForbiddenError(f"User id {self.data['user'].id} has no rights")
        else:
            pass

    def _check_user_role(self):
        if self.data["user"].is_superuser or self.data["user"].is_staff:
            return True
        else:
            self.errors["user"] = ForbiddenError(f"User id {self._user.id} has no rights")

    def _check_post_presence(self):
        if self._post:
            pass
        else:
            self.errors["post_id"] = ObjectDoesNotExist(f"Post pk {self.cleaned_data['post_id']} not found")
