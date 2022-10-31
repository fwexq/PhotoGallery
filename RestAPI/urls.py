from django.urls import path
from RestAPI.views.comment.create import CommentAddListView
from RestAPI.views.comment.detailUpdateDestroy import CommentDetailUpdateDestroyView
from RestAPI.views.post.create import PostListCreate
from RestAPI.views.post.detailUpdateDestroy import PostDetailUpdateDestroyView
from RestAPI.views.user.detail import UserDetailView
from RestAPI.views.user.update import UserUpdateView

urlpatterns = [
    path('post/', PostListCreate.as_view(), name='create_posts'),  #Просмотр всех постов и создание поста
    path('post/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_post'), #Просмотр, обновление, удаление поста

    path('user/current/', UserDetailView.as_view(), name='current_user'), #Просмотр текущего пользователя и получение токена
    path('user/<int:pk>/', UserUpdateView.as_view(), name='update_current_user'), #Изменение профиля


    path('comment/', CommentAddListView.as_view(), name='create_comment'), #Просмотр всех комментариев и создание комментария
    path('comment/<int:pk>/', CommentDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_comment'), #Просмотр, обновление, удаление комментария
   ]






   # path('user/role/<int:pk>/', CustomUserChangeRoleView.as_view(), name='change_role'), #Изменение прав у пользователя

    # path('post/invalid/<int:post_id>/', PostInvalidView.as_view(), name='invalid'), #Устанавливает посту статус "Отклонен"
    # path('post/valid/<int:post_id>/', PostValidView.as_view(), name='valid'), #Устанавливает посту статус "Одобрен"



    # path('likes/<int:pk>', PostAddLikeView.as_view(), name='likes'), #Устанавливает лайк