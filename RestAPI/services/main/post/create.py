from django import forms
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import CustomUser, Post
from service_objects.fields import ModelField

class CreatePostService(Service):
    title = forms.CharField(required=True, max_length=40)
    description = forms.CharField(required=True, max_length=80)
    photo = forms.ImageField(required=True)
    user = ModelField(CustomUser)

    def process(self):
        self._check_user_rights()
        self._create_post()
        self.result = self._create_post()
        return self

    def _create_post(self):
        self.post = Post(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            photo=self.cleaned_data['photo'],
            author=self.cleaned_data['user']
        )
        self.post.save()
        return self.post
    def _check_user_rights(self):
        if not self.cleaned_data['user'].is_authenticated:
            self.errors["user"] = ForbiddenError(f"User id {self.cleaned_data['user'].id} does not exist")