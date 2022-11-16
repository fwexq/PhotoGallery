from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from main.models import CustomUser, Post


class PostCancelDeleteService(Service):
    post_id = forms.IntegerField()
    user = ModelField(CustomUser)

    def process(self):
        post = Post.objects.get(pk=self.cleaned_data['post_id'])
        post.moderation_status = 'VALID'
        post.save()


