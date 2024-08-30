from django.urls import include, path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('api/', include('api.urls')),
]