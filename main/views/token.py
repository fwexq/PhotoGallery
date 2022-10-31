from django.shortcuts import render
from django.views import View

from RestAPI.services.main.user.token import TokenService
from ..forms import *



class TokenView(View):
    model = CustomUser

    def post(self, request, *args, **kwargs):
        token = TokenService.execute({'user': request.user})
        return render(request, 'main/accounts/profile.html', {'token': token})
