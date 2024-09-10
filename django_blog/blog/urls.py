from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('post/', include([
        path('', views.PostListView.as_view(), name='post_list'),
        path('new/', views.PostCreateView.as_view(), name='post_create'),
        path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
        path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
        path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    ])),
]