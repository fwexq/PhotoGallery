from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post, Like


class LikesService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()

    def process(self):
        try:
            like = Like.objects.get(user=self.cleaned_data['user'], post_id=self.cleaned_data['post_id'])
        except Like.DoesNotExist:
            Like.objects.create(user=self.cleaned_data['user'], post_id=self.cleaned_data['post_id'])
            is_likes = True
        else:
            like.delete()
            is_likes = False

        # post.save()
        return is_likes