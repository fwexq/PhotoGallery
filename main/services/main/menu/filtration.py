

from django import forms
from django.db.models import Count
from service_objects.services import Service
from main.models import Post


class PostFiltrationService(Service):
    date_filter = forms.CharField(required=True)

    def process(self):
        match self.cleaned_data['date_filter']:
            case "by likes":
                return Post.objects.filter(moderation_status='VALID').annotate(cnt=Count('likes')).order_by('-cnt')
            case "by comments":
                return Post.objects.filter(moderation_status='VALID').annotate(cnt=Count('comments')).order_by('-cnt')
            case "by date":
                return Post.objects.filter(moderation_status='VALID').order_by('-publicated_at')



