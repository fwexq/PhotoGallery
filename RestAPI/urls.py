from django.urls import path
from RestAPI.views.comment.create import CommentAddListView
from RestAPI.views.post.createView import PostAddListView
from RestAPI.views.post.detailUpdateDestroy import PostDetailUpdateDestroyView
from RestAPI.views.user.detail_view import UserDetailView

urlpatterns = [
    path('posts/', PostAddListView.as_view(), name='add_posts'), #Создание поста и просмотр всех постов
    path('user/info/', UserDetailView.as_view(), name='current_user'), #Текущий пользователь
    path('comments/', CommentAddListView.as_view(), name='create_comment'), #Создание комментария
    path('post/detailUpdateDestroy/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='detailUpdateDestroy'), #Просмотр, обновление, удаление поста

]