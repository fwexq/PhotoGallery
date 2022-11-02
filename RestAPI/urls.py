from django.urls import path

from RestAPI.views.admin.customUserChangeRole import CustomUserChangeRoleView
from RestAPI.views.comment.listCreate import CommentListCreateView
from RestAPI.views.comment.detailUpdateDestroy import CommentDetailUpdateDestroyView
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
   ]



    # path('post/invalid/<int:post_id>/', PostInvalidView.as_view(), name='invalid'), #Устанавливает посту статус "Отклонен"
    # path('post/valid/<int:post_id>/', PostValidView.as_view(), name='valid'), #Устанавливает посту статус "Одобрен"



    # path('likes/<int:pk>', PostAddLikeView.as_view(), name='likes'), #Устанавливает лайк