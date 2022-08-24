from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post, Like


class LikesService(Service):
    user = ModelField(CustomUser)
    pk = forms.CharField(required=True)

    def process(self):
        self.like = Like(
            user=self.cleaned_data['user'],
            pk=self.cleaned_data['pk']
        )
        post = Post.objects.get(pk=self.cleaned_data['pk'])
        if self.cleaned_data['user'] in post.liked.all():
            post.liked.remove(self.cleaned_data['user'])
            is_liked = False
        else:
            post.liked.add(self.cleaned_data['user'])
            is_liked = True
        post.save()
        return is_liked