from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..forms import *


class CreateStaff(View):
    model = CustomUser
    context_object_name = 'title'
    template_name = 'main/job_title/create_staff.html'
    form_class = CreateJobTitle

    def post(self, request, *args, **kwargs):
        post_form = CreateJobTitle(request.POST)
        if post_form.is_valid():
            users = CustomUser.objects.filter(id__in=post_form.cleaned_data['id'])
            users.update(is_superuser=post_form.cleaned_data['is_superuser'],
                         is_staff=post_form.cleaned_data['is_staff'])
            return redirect('posts_list')


    def get(self, request):
        form = CreateJobTitle()
        return render(request, 'main/job_title/create_staff.html', {'form': form})
