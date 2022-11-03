from django import forms
from service_objects.services import Service
from service_objects.fields import ModelField
from main.models import CustomUser


class ProfileUpdateService(Service):
    first_name = forms.CharField(required=False, max_length=255)
    last_name = forms.CharField(required=False, max_length=255)
    avatar = forms.ImageField(required=False, max_length=1024)
    user = ModelField(CustomUser)

    def process(self):
        user = self.cleaned_data['user']
        if self.cleaned_data['first_name']:
            user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data['last_name']:
            user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['avatar']:
            user.avatar = self.cleaned_data['avatar']
        user.save()
        return self
