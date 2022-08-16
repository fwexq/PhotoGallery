from django.shortcuts import render
from django.views import View
from ..forms import *
from rest_framework.authtoken.models import Token

class TokenView(View):
    model = CustomUser
    form_class = TokenForm

    def post(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        if user.api_key:
            Token.objects.get(user_id=request.user.id).delete()
        user.api_key = Token.objects.create(user=request.user).key
        user.save()
        return render(request, 'main/accounts/profile.html')

    def get(self, request):
        form = TokenForm()
        return render(request, 'main/accounts/profile.html', {'form': form})
