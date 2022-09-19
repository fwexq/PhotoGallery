from rest_framework.response import Response
from rest_framework import generics
from ..serializers import PostSerializer
from ..services.main.search import SearchService


class Search(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        outcome = SearchService.execute(self.request.query_params.dict())
        return Response({'posts': PostSerializer(outcome, many=True).data})
