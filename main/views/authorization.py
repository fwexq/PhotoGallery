import os
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from ..forms import *
from main.utils import DataMixin



class AuthorizationView(DataMixin, TemplateView):
    template_name = os.path.join('main/accounts', 'authorizations.html')
    redirect_authenticated_user = True
    sign_up_form_class = RegisterUserForm
    sign_in_form_class = LoginUserForm

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        sign_up_form = self.sign_up_form_class()
        sign_in_form = self.sign_in_form_class()
        context['sign_up_form'] = kwargs.get('sign_up_form', sign_up_form)
        context['sign_in_form'] = kwargs.get('sign_in_form', sign_in_form)
        return context

    def sign_up_form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse_lazy('profile'))

    def sign_in_form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(reverse_lazy('posts_list'))

    def post(self, request):
        post_data = request.POST or None
        sign_up_form = self.sign_up_form_class(data=post_data)
        sign_in_form = self.sign_in_form_class(data=post_data)
        context = self.get_context_data(sign_up_form=sign_up_form,
                                        sign_in_form=sign_in_form)
        if post_data.get('action') == 'sign_up':
            if sign_up_form.is_valid():
                return self.sign_up_form_valid(sign_up_form)
        if post_data.get('action') == 'sign_in':
            if sign_in_form.is_valid():
                return self.sign_in_form_valid(sign_in_form)
            else:
                return self.render_to_response(context)
        return self.render_to_response(context)