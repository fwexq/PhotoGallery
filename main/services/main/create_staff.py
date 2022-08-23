from django import forms
from service_objects.services import Service
from main.models import CustomUser


class CreateStaffService(Service):
    id = forms.CharField(required=True, max_length=255)
    is_superuser = forms.CharField(required=False)
    is_staff = forms.CharField(required=False)

    def process(self):
        is_superuser = True if self.cleaned_data.get('is_superuser') == 'on' else False
        is_staff = True if self.cleaned_data.get('is_staff') == 'on' else False
        users = CustomUser.objects.filter(id__in=self.cleaned_data['id'])
        users.update(is_superuser=is_superuser,
                     is_staff=is_staff)
        return self