from django import forms
from django.db.models import Q
from service_objects.services import Service
from main.models import Post


class SearchService(Service):
    search = forms.CharField()
    def process(self):
        res_search = self.cleaned_data.get('search', "")
        results = Post.objects.filter((Q(title__icontains=res_search)
                                       | Q(description__icontains=res_search)))
        return results