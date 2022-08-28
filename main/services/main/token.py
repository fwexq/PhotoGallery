# from django import forms
# from service_objects.fields import ModelField
# from service_objects.services import Service
# from main.models import *
#
#
# class TokenService(Service):
#     user = ModelField(CustomUser)
#     def process(self):
#         self.token = Token(
#             user_id=self.cleaned_data['user'],
#         )
#         token = Token.objects.filter(user_id=self.cleaned_data['user'])
#         if token:
#             Token.objects.get(user_id=self.cleaned_data['user']).delete()
#         token = Token.objects.create(self.cleaned_data['user'])
#         token.save()
#
#


