from django import forms
from service_objects.services import Service
from main.models import CustomUser


class RoleAssignmentService(Service):
    id = forms.IntegerField()
    is_staff = forms.CharField()

    def process(self):
        is_staff = True if self.cleaned_data.get('is_staff') == 'on' else False
        users = CustomUser.objects.filter(id__in=self.cleaned_data['id'])
        users.update(is_staff=is_staff, )
        return self