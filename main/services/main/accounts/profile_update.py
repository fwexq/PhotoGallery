# from service_objects.services import Service
# from service_objects.fields import ModelField
#
# from main.models import CustomUser
#
#
# class ProfileUpdateService(Service):
#     user = ModelField(CustomUser)
#
#     def process(self):
#         user = CustomUser.objects.get(pk=self.cleaned_data['user'].id)
#         if
#         #
#         #     # self.object = self.get_object()
#         # form = self.get_form()
#         # if form.is_valid():
#         #     return self.form_valid(form)
#         #
#         # else:
#         #     return self.form_invalid(form)
#
#         return user