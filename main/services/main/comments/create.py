from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post, Comment


class CommentsCreateService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()
    text = forms.CharField()
    parent = forms.IntegerField(required=False)

    def process(self):
        comment = Comment(
            text=self.cleaned_data['text'],
            user=self.cleaned_data['user'],
            post_id=self.cleaned_data['post_id']
        )
        if self.cleaned_data['parent']:
            comment.parent_id = self.cleaned_data['parent']
        comment.save()

