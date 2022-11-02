from service_objects.fields import ModelField
from service_objects.services import Service
from main.models import CustomUser


class UserGetService(Service):
    user = ModelField(CustomUser)

    def process(self):
        self.result = self.cleaned_data["user"]
        return self


