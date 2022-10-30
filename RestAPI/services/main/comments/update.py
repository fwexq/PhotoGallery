from django import forms
from django.shortcuts import get_object_or_404
from service_objects.services import Service
from main.models import Comment


class CommentUpdateService(Service):
    pk = forms.IntegerField()
    text = forms.CharField(required=True, max_length=255)

    def process(self):
        comment = get_object_or_404(Comment, pk=self.cleaned_data['pk'])
        if self.cleaned_data['text']:
            comment.text = self.cleaned_data['text']
        comment.save()
        return comment


