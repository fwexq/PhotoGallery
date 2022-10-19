from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service


from main.models import CustomUser, Post, Comment


class CommentsCreateService(Service):
    user = ModelField(CustomUser)
    post_id = forms.IntegerField()
    text = forms.CharField()
    parent = forms.CharField(required=False)

    def process(self):
        self.comment = Comment(
            text=self.cleaned_data['text'],
            user=self.cleaned_data['user']
        )
        self.comment.post = Post.objects.get(pk=self.cleaned_data['post_id'])
        parent = self.cleaned_data['parent']
        if parent:
            self.comment.parent = Comment.objects.get(id=int(parent))
        self.comment.save()

