from django.urls import path

from RestAPI.views.admin.customUserChangeRole import CustomUserChangeRoleView
from RestAPI.views.comment.create import CommentAddListView
from RestAPI.views.comment.detailUpdateDestroy import CommentDetailUpdateDestroyView
from RestAPI.views.comment.view import CommentsListView
from RestAPI.views.post.create import PostAddView
from RestAPI.views.post.detailUpdateDestroy import PostDetailUpdateDestroyView
# from RestAPI.views.post.likes import PostAddLikeView
from RestAPI.views.post.valid_or_invalid_posts import PostInvalidView, PostValidView
from RestAPI.views.post.view import PostsListView
from RestAPI.views.user.detail import UserDetailView
from RestAPI.views.user.token import UserCreateTokenView
from RestAPI.views.user.update import UserUpdateView

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts'), #Просмотр всех постов
    path('posts/create/', PostAddView.as_view(), name='add_posts'), #Создание поста

    # path('posts/', PostListCreate.as_view(), name='add_posts'), #Просмотр всех постов и создание поста
    # path('posts/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_post'),

    path('post/detailUpdateDestroy/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_post'), #Просмотр, обновление, удаление поста

    # path('user/current/', UserDetailView.as_view(), name='current_user'), #Просмотр текущего пользователя объед с токеном
    # path('user/<int:pk>/', UserDetailView.as_view(), name='current_user'), #Просмотр любого пользователя

    path('user/info/', UserDetailView.as_view(), name='current_user'), #Просмотр текущего пользователя
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='update_current_user'), #Изменение профиля
    # path('user/<int:pk>/', UserUpdateView.as_view(), name='update_current_user'),  # Изменение профиля

    path('user/token/<int:pk>/', UserCreateTokenView.as_view(), name='create_token'), #Получение токена
    path('comment/create/', CommentAddListView.as_view(), name='create_comment'), #Создание комментария
    path('comments/', CommentsListView.as_view(), name='create_comment'), #Просмотр всех комментариев
    path('comment/detailUpdateDestroy/<int:pk>/', CommentDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy_comment'), #Просмотр, обновление, удаление комментария

    # path('user/role/<int:pk>/', CustomUserChangeRoleView.as_view(), name='change_role'), #Изменение прав у пользователя

    # path('post/invalid/<int:post_id>/', PostInvalidView.as_view(), name='invalid'), #Устанавливает посту статус "Отклонен"
    # path('post/valid/<int:post_id>/', PostValidView.as_view(), name='valid'), #Устанавливает посту статус "Одобрен"

    # path('likes/<int:pk>', PostAddLikeView.as_view(), name='likes'), #Устанавливает лайк

]