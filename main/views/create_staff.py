from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..forms import *
from ..services.main.create_staff import CreateStaffService


class CreateStaff(View):
    template_name = 'main/job_title/create_staff.html'
    form_class = CreateJobTitle

    def post(self, request, *args, **kwargs):
        CreateStaffService.execute(request.POST)
        return redirect('posts_list')

    def get(self, request):
        form = CreateJobTitle()
        return render(request, 'main/job_title/create_staff.html', {'form': form})
