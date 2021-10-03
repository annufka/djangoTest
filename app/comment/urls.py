from django.urls import path

from app.comment import views

urlpatterns = [
    path("comment/", views.CommentView.as_view(), name="comment"),
    path("comment/<int:pk>/", views.CommentView.as_view(), name="comment"),
]
