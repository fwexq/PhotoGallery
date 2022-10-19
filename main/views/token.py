from django.shortcuts import render
from django.views import View
from ..forms import *
from main.services.main.accounts.token import TokenService


class TokenView(View):
    model = CustomUser

    def post(self, request, *args, **kwargs):
        token = TokenService.execute({'user': request.user})
        return render(request, 'main/accounts/profile.html', {'token': token})
