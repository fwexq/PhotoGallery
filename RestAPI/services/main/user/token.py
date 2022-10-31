from functools import lru_cache

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from service_objects.fields import ModelField
from service_objects.services import Service

from RestAPI.errors import ForbiddenError
from main.models import CustomUser


class TokenService(Service):
    user = ModelField(CustomUser)
    def process(self):
        self._check_user_presence()
        if self._user:
            self.result = self._create_token()
        return self

    @property
    @lru_cache
    def _user(self):
        try:
            return CustomUser.objects.get(pk=self.cleaned_data["user"].id)
        except ObjectDoesNotExist:
            return None

    def _create_token(self):
        Token.objects.filter(user=self._user).delete()
        return Token.objects.create(user=self._user)

    def _check_user_presence(self):
        if self._user:
            pass
        else:
            self.errors["user"] = ForbiddenError(f"User id {self._user} does not exist")