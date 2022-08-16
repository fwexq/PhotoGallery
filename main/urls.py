from django.urls import path
from .views.authorization import AuthorizationView
from .views.comments import CommentsView
from .views.create_staff import CreateStaff
from .views.for_approval_posts import PostModerationListView
from .views.likes import LikesView
from .views.logouster import ProfileLogoutView
from .views.posts import PostListView, PostUpdateView, PostDeleteView, DetailPostView, CreatePostView
from .views.valid_or_invalid_posts import PostInvalidView, PostValidView
from .views.profile import ProfileView, ProfileUpdateView
from .views.search import Search
from .views.status_posts import PostStatusView
from .views.token import TokenView


urlpatterns = [

    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    path('token/', TokenView.as_view(), name='token'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update'),

    path('', PostListView.as_view(), name='posts_list'),
    path('create/', CreatePostView.as_view(), name='posts_create'),
    path('update/<int:det>/', PostUpdateView.as_view(), name='posts_update'),
    path('delete/<int:det>/', PostDeleteView.as_view(), name='posts_delete'),
    path('detail/<int:det>/', DetailPostView.as_view(), name='posts_detail'),
    path('post/moderation/', PostModerationListView.as_view(), name='post_list_moderation'),


    path('posts/<str:status>/', PostStatusView.as_view(), name='account_posts_list'),


    path('detail/<int:det>/comments/', CommentsView.as_view(), name='comments'),
    path('likes/<int:pk>', LikesView.as_view(), name='posts_like'),
    path('invalid/<int:det>/', PostInvalidView.as_view(), name='invalid'),
    path('valid/<int:det>/', PostValidView.as_view(), name='valid'),
    path('search/', Search.as_view(), name='search'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),

    path('create_staff/', CreateStaff.as_view(), name='create_staff'),

]

