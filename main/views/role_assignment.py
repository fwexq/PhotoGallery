from django.shortcuts import render, redirect
from django.views import View

from RestAPI.services.main.admin.role_assignment import CustomUserChangeRoleServices
from ..forms import *


class RoleAssignmentView(View):
    template_name = 'main/admin/role_assignment.html'
    form_class = RoleAssignment

    def post(self, request, *args, **kwargs):
        CustomUserChangeRoleServices.execute(request.POST)
        return redirect('posts_list')

    def get(self, request):
        return render(request, 'main/admin/role_assignment.html', {'form': RoleAssignment()})
