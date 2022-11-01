from functools import lru_cache
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import Service
from main.models import Comment


class CommentListService(Service):

    def process(self):
        self._check_comments_presence()
        self.result = self._comments
        return self

    @property
    @lru_cache
    def _comments(self):
        try:
            return Comment.objects.all()
        except ObjectDoesNotExist:
            return None

    def _check_comments_presence(self):
        if not self._comments:
            self.errors["pk"] = ObjectDoesNotExist("Comments not found")