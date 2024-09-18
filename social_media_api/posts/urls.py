from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, FeedView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view()),
]