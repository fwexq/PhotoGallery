from django import forms
from service_objects.services import Service
from main.models import CustomUser, Post
from service_objects.fields import ModelField

class CreatePostService(Service):
    title = forms.CharField(required=True, max_length=40)
    description = forms.CharField(required=True, max_length=80)
    photo = forms.ImageField(required=False)
    user = ModelField(CustomUser)

    def process(self):
        if self.cleaned_data['user'].is_authenticated:
            self.post = Post(
                title=self.cleaned_data['title'],
                description=self.cleaned_data['description'],
                photo=self.cleaned_data['photo'],
                author=self.cleaned_data['user']
            )
            self.post.save()
            return self.post
        else:
            return f'Authentication credentials were not provided'
