from django.shortcuts import render
from django.views import View
from ..forms import *
from ..services.main.token import TokenService


class TokenView(View):
    model = CustomUser

    def post(self, request, *args, **kwargs):
        token = TokenService.execute({'user': request.user})
        # token = Token.objects.filter(user_id=request.user.id)
        # if token:
        #     Token.objects.get(user_id=request.user.id).delete()
        # token = Token.objects.create(user=request.user)
        # token.save()
        return render(request, 'main/accounts/profile.html', {'token': token})

    # def get(self, request):
    #     form = TokenForm()
    #     return render(request, 'main/accounts/profile.html', {'form': form})
