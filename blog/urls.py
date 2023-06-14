from django.urls import path

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    MyPostView
                    )
from . import views


urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('user/<str:username>',MyPostView.as_view(), name='user_posts'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('post/new/',PostCreateView.as_view(), name='post_create'),
    path('about/',views.about, name='blog-about'),

]
