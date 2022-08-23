# from django import forms
# from service_objects.services import Service
# from main.models import CustomUser
#
#
# class AuthorizationService(Service):
#     first_name = forms.CharField(required=True, max_length=255)
#     email = forms.CharField(required=True, max_length=255)
#     password = forms.CharField(required=True, max_length=255)
#
#     def process(self):
#         self.user = CustomUser(
#             first_name=self.cleaned_data['first_name'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#         )
#         # self.post.save()
#         return self.user