from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser, Post


class DeletePostService(Service):
    pk = forms.IntegerField()
    user = ModelField(CustomUser)

    def process(self):
        try:
            Post.objects.get(pk=self.cleaned_data['pk'])
        except:
                message = f"Post {self.cleaned_data['pk']} not found"
        else:
            if self.cleaned_data['user'].id == Post.objects.get(pk=self.cleaned_data['pk']).author.id:
                Post.objects.get(pk=self.cleaned_data['pk']).delete()
                message = f"Post {self.cleaned_data['pk']} has been deleted"
            else:
                message = f"You are not the creator of the post {self.cleaned_data['pk']}"
        return message
