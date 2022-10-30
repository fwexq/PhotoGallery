from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Comment


class DeleteCommentService(Service):
    pk = forms.IntegerField()
    user = ModelField(CustomUser)

    def process(self):
        try:
            Comment.objects.get(pk=self.cleaned_data['pk'])
        except:
                message = f"Comment {self.cleaned_data['pk']} not found"
        else:
            if self.cleaned_data['user'].id == Comment.objects.get(pk=self.cleaned_data['pk']).user.id:
                Comment.objects.get(pk=self.cleaned_data['pk']).delete()
                message = f"Comment {self.cleaned_data['pk']} has been deleted"
            else:
                message = f"You are not the creator of the comment {self.cleaned_data['pk']}"
        return message
