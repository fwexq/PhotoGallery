from functools import lru_cache
from django.core.exceptions import ObjectDoesNotExist
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser


class UserGetService(Service):
    user = ModelField(CustomUser)

    def process(self):
        self.result = self._user
        return self

    @property
    def _user(self):
        try:
            return CustomUser.objects.get(pk=self.cleaned_data["user"].id)
        except ObjectDoesNotExist:
            return None
