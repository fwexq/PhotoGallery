from rest_framework.authtoken.models import Token
from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser


class TokenService(Service):
    user = ModelField(CustomUser)
    def process(self):
        if self.cleaned_data['user'].is_authenticated:
            if self.cleaned_data['user'].pk == self.data['pk']:
                Token.objects.filter(user=self.cleaned_data['user']).delete()
                return Token.objects.create(user=self.cleaned_data['user'])
            else:
                f'Account does not belong to you'
        else:
            return f'Authentication credentials were not provided'
