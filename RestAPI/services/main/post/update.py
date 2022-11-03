from functools import lru_cache
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from RestAPI.errors import ForbiddenError
from main.models import Post, CustomUser
from django.db import transaction, DatabaseError, IntegrityError


class PostUpdateService(Service):
    post_id = forms.IntegerField()
    title = forms.CharField(required=False, max_length=40)
    description = forms.CharField(required=False, max_length=80)
    photo = forms.ImageField(required=False)
    moderation_status = forms.ChoiceField(required=False, choices=Post.MODERATION_CHOICES)
    user = ModelField(CustomUser)

    def process(self):
        self._check_post_presence()
        if self._post:
            try:
                with transaction.atomic():
                    self._check_user_rights()
                    self._update_post()
                    if self.cleaned_data["moderation_status"]:
                        self._check_user_can_change_status()
                        if self.errors:
                            raise IntegrityError
                        else:
                            self._update_moderation_status()
                            self.result = self._post
                    else:
                        self.result = self._post
            except (DatabaseError, IntegrityError):
                return self
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
        self._post.moderation_status = self.cleaned_data['moderation_status']
        self._post.save()


    def _check_user_rights(self):
        if not self.cleaned_data['user'].id == self._post.author_id:
            self.errors["user"] = ForbiddenError("You are not allowed to make this action")

    def _check_user_can_change_status(self):
        if not (self.data["user"].is_superuser or self.cleaned_data["user"].is_staff):
            self.errors["user"] = ForbiddenError("Only moderators can change status")



    def _check_post_presence(self):
        if not self._post:
            self.errors["post_id"] = ObjectDoesNotExist(f"Post pk {self.cleaned_data['post_id']} not found")

    # def _add_like(self):
    #     self.like = Like(
    #         user=self.cleaned_data['user'],
    #         post_id=self.cleaned_data['pk']
    #     )
    #     post = self._post
    #     if self.cleaned_data['user'] in post.liked.all():
    #         post.liked.remove(self.cleaned_data['user'])
    #         is_liked = False
    #     else:
    #         post.liked.add(self.cleaned_data['user'])
    #         is_liked = True
    #     post.save()
    #     outcome = is_liked
    #     return outcome
