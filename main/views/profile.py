from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from ..forms import *


class ProfileView(ListView):
    model = CustomUser
    template_name = 'main/accounts/profile.html'
    context_object_name = 'prof'

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs['pk'])
        return render(request, 'main/accounts/profile.html', {'user': user})


class ProfileUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'main/accounts/profile_update.html'

    def get_object(self):
        return self.model.objects.get(id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        # self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})
