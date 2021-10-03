from django.urls import path

from app.post import views

# https://www.getpostman.com/collections/9da7c4ad5747d2137ebc

urlpatterns = [
    path("get/posts/", views.PostsViewGet.as_view(), name="posts"),
    path("post/", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/", views.PostView.as_view(), name="post"),
    # path('create/post/', views.PostViews.as_view(), name='create_post'),
    path("post/upvote/<int:pk>/", views.PostUpvote.as_view(), name="upvote"),
]
