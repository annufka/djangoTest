from rest_framework import serializers

from app.comment.models import Comment


class CommentGetSerializer(serializers.Serializer):
    author_name = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    creation_date = serializers.DateTimeField(required=False)


class CommentSerializer(serializers.Serializer):
    author_name = serializers.CharField()
    content = serializers.CharField()
    creation_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
