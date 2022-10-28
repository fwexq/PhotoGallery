from django import forms
from service_objects.services import Service
from main.models import CustomUser

# CustomUserChangeRoleServices
# ActionUpdateService
class RoleAssignmentService(Service):
    user = forms.MultipleChoiceField(choices=[(item.pk, item) for item in CustomUser.objects.all()])
    is_staff = forms.CharField()

    def process(self):
        is_staff = True if self.cleaned_data.get('is_staff') == 'on' else False
        users = CustomUser.objects.filter(id__in=self.cleaned_data['user'])
        users.update(is_staff=is_staff, )