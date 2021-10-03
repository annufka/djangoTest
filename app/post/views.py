from copy import copy

from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.post import serializers
from app.post.models import Post
from app.post.serializers import PostSerializer


# этого по заданию вроде не надо, но я почему-то по
# привычке с этого начала и жалко удалить)
class PostsViewGet(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = serializers.PostGetSerializer(posts, many=True)
        return Response(serializer.data)


class PostView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Exception:
            raise Http404
        serializer = serializers.PostGetSerializer(post)
        return Response(serializer.data)

    def post(self, request):
        data = copy(request.data)
        data["author_name"] = request.user.username
        # print(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data
        serializer = PostSerializer(
            instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response(
            {"message": "Post with id `{}` has been deleted.".format(pk)},
            status=204
        )


class PostUpvote(APIView):
    def put(self, request, pk):
        # тут через try/except потому что если нет поста, то смысл
        # его создавать и голосовать за него
        try:
            post = Post.objects.get(pk=pk)
        except Exception:
            return Response(status=404)
        data = copy(request.data)
        data["amount_of_upvotes"] = post.amount_of_upvotes + 1
        serializer = PostSerializer(instance=post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
