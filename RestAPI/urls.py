from django.urls import path
from RestAPI.views.comment.listCreate import CommentListCreateView
from RestAPI.views.comment.detailUpdateDestroy import CommentDetailUpdateDestroyView
from RestAPI.views.like.create import PostAddLikeView
from RestAPI.views.like.delete import PostDeleteLikeView
from RestAPI.views.post.listCreate import PostListCreateView
from RestAPI.views.post.detailUpdateDestroy import PostDetailUpdateDestroyView
from RestAPI.views.user.detail import UserDetailView
from RestAPI.views.user.update import UserUpdateView

urlpatterns = [
    path('post/', PostListCreateView.as_view(), name='create_posts'),  #Просмотр всех постов и создание поста
    path('post/<int:post_id>/', PostDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_post'), #Просмотр, обновление, удаление поста

    path('user/current/', UserDetailView.as_view(), name='current_user'), #Просмотр текущего пользователя и получение токена
    path('user/<int:pk>/', UserUpdateView.as_view(), name='update_current_user'), #Изменение профиля, прав пользователя


    path('comment/', CommentListCreateView.as_view(), name='create_comment'), #Просмотр всех комментариев и создание комментария
    path('comment/<int:post_id>/', CommentDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_comment'), #Просмотр, обновление, удаление комментария

    path('create/like/<int:post_id>/', PostAddLikeView.as_view(), name='likes'), #Устанавливает лайк
    path('delete/like/<int:post_id>/', PostDeleteLikeView.as_view(), name='likes'), #Снимает лайк
   ]


# def put(self, request, *args, **kwargs):
# return Response({"Error": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


