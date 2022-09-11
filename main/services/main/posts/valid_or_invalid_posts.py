from django import forms
from django.utils import timezone
from service_objects.services import Service

from main.models import Post


class PostInvalidService(Service):
    det = forms.IntegerField()

    def process(self):
        post = Post.objects.get(pk=self.cleaned_data['det'])
        post.moderation_status = 'INVALID'
        post.save()
        return self


class PostValidService(Service):
    det = forms.IntegerField()

    def process(self):
        post = Post.objects.get(pk=self.cleaned_data['det'])
        post.moderation_status = 'VALID'
        post.publicated_at = timezone.now()
        post.save()
        return self