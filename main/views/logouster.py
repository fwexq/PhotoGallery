from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

class ProfileLogoutView(LogoutView):
    def logoutuser(request):
        logout(request)
        return redirect('posts_list')