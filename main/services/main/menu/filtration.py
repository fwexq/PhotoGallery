
from django import forms
from django.db.models import Count
from service_objects.services import Service
from main.models import Post


class PostFiltrationService(Service):
    ORDER_MAPPER = {"asc": '', "desc": '-'}
    sort_by = forms.CharField(required=True)

    def process(self):
        if self._sort_field:
            if "likes" or "comments":
                return Post.objects.filter(moderation_status='VALID').annotate(cnt=Count(self._sort_field)).order_by \
                    (f'{self._sort_order}cnt')
            elif "date":
                return Post.objects.filter(moderation_status='VALID').order_by(f'{self._sort_order}publicated_at')
    @property
    def _sort_field(self):
        return self.cleaned_data['sort_by'].split('_')[0]

    @property
    def _sort_order(self):
        return self.ORDER_MAPPER[self.cleaned_data['sort_by'].split('_')[1]]







    # def process(self):
    #     if self._sort_field:
    #         if "likes" or "comments":
    #             return Post.objects.filter(moderation_status='VALID').annotate(cnt=Count(self._sort_field)).order_by \
    #                 (f'{self._sort_order}cnt')
    #         elif "date":
    #             return Post.objects.filter(moderation_status='VALID').order_by(f'{self._sort_order}publicated_at')
    # @property
    # def _sort_field(self):
    #     return self.cleaned_data['sort_by'].split('_')[0]
    #
    # @property
    # def _sort_order(self):
    #     return self.ORDER_MAPPER[self.cleaned_data['sort_by'].split('_')[1]]
