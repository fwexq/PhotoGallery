from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import *


class TokenService(Service):
    user = ModelField(CustomUser)

    def process(self):
        self.token = Token(
            user=self.cleaned_data['user']
        )
        user = CustomUser.objects.get(id=self.cleaned_data['user'].id)
        if self.cleaned_data['user'].api_key:
            Token.objects.get(user_id=self.cleaned_data['user']).delete()
        self.cleaned_data['user'].api_key = Token.objects.create(user=self.cleaned_data['user']).key
        user.save()
        return self.token
