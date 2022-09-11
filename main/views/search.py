from rest_framework.response import Response
from rest_framework import generics
from ..serializers import PostSerializer
from ..services.main.search import SearchService


class Search(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        outcome = SearchService.execute(self.request.query_params.dict())
        # res_search = self.request.query_params.get('search', "")
        # results = Post.objects.filter((Q(title__icontains=res_search)
        #                                | Q(description__icontains=res_search)))

        return Response({'posts': PostSerializer(outcome, many=True).data})
