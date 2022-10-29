from django import forms
from django.shortcuts import get_object_or_404
from service_objects.services import Service
from main.models import Post

class PostUpdateService(Service):
    pk = forms.IntegerField()
    title = forms.CharField(required=False, max_length=40)
    description = forms.CharField(required=False, max_length=80)
    photo = forms.ImageField(required=False)

    def process(self):
        post = get_object_or_404(Post, pk=self.cleaned_data['pk'])
        if self.cleaned_data['title']:
            post.title = self.cleaned_data['title']
        if self.cleaned_data['description']:
            post.description = self.cleaned_data['description']
        if self.cleaned_data['photo']:
            post.previous_photo = post.photo
            post.photo = self.cleaned_data['photo']
        post.moderation_status = 'NOT_MODERATED'
        # post.publicated_at = timezone.now()
        post.save()
        return post


