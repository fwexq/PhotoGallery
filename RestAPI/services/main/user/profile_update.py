from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service
from service_objects.fields import ModelField

from RestAPI.errors import ForbiddenError
from main.models import CustomUser


class ProfileUpdateService(Service):
    first_name = forms.CharField(required=False, max_length=255)
    last_name = forms.CharField(required=False, max_length=255)
    avatar = forms.ImageField(required=False, max_length=1024)
    user = ModelField(CustomUser)
    is_staff = forms.CharField(required=False)

    def process(self):
        self._check_user_presence()
        if self._user:
            self._check_user_rights()
            self._update_profile()
            if self._check_user_role():
                user = self._change_user_role()
                self.result = user
            else:
                self.result = self._user
        return self

    @property
    @lru_cache()
    def _user(self):
        try:
            return CustomUser.objects.get(pk=self.cleaned_data["user"].id)
        except ObjectDoesNotExist:
            return None

    def _update_profile(self):
        if self.cleaned_data['first_name']:
            self._user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data['last_name']:
            self._user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['avatar']:
            self._user.avatar = self.cleaned_data['avatar']
        self._user.save()

    def _check_user_rights(self):
        if not self._user.id == self.data["pk"]:
            self.errors["user"] = ForbiddenError(f"User id {self._user.id} has no rights")

    def _check_user_presence(self):
        if not self._user:
            self.errors["user"] = ObjectDoesNotExist(f"User {self._user} does not have enough rights")
        else:
            pass

    def _change_user_role(self):
        is_staff = True if self.cleaned_data.get('is_staff') == 'On' else False
        user = CustomUser.objects.get(id=self.cleaned_data['user'].id)
        user.is_staff = is_staff
        user.save()
        return user

    def _check_user_role(self):
        if self.cleaned_data["user"].is_superuser or self.cleaned_data["user"].is_staff:
            return True
        else:
            self.errors["user"] = ForbiddenError(f"User id {self._user.id} has no rights")


