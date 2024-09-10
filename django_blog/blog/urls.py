from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/', views.CommentListView.as_view(), name='comment_list'),
    path('post/<int:post_id>/comment/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:post_id>/comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('post/<int:post_id>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]