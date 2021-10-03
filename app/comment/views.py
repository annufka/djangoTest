from copy import copy

from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.comment import serializers
from app.comment.models import Comment
from app.comment.serializers import CommentSerializer


class CommentView(APIView):
    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
        except Exception:
            raise Http404
        serializer = serializers.CommentGetSerializer(comment)
        return Response(serializer.data)

    def post(self, request):
        data = copy(request.data)
        data["author_name"] = request.user.username
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_comment = get_object_or_404(Comment.objects.all(), pk=pk)
        data = request.data
        serializer = CommentSerializer(
            instance=saved_comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response(
            {"message": "Comment with id `{}` has been deleted.".format(pk)},
            status=204
        )
