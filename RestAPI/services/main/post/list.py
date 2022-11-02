from service_objects.services import Service
from main.models import Post


class PostListService(Service):
    def process(self):
        self.result = Post.objects.filter(moderation_status="VALID")
        return self





