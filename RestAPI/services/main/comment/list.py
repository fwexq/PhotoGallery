from service_objects.services import Service

from main.models import Comment


class CommentListService(Service):
    def process(self):
        self.result = Comment.objects.all()
        return self