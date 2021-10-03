from rest_framework import serializers

from app.post.models import Post


class PostGetSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    link = serializers.CharField(required=False)
    creation_date = serializers.DateTimeField(required=False)
    amount_of_upvotes = serializers.IntegerField(required=False)
    author_id = serializers.IntegerField(required=False)


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    link = serializers.CharField()
    creation_date = serializers.DateTimeField(required=False)
    amount_of_upvotes = serializers.IntegerField(required=False)
    author_name = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.link = validated_data.get("link", instance.link)
        instance.amount_of_upvotes = validated_data.get(
            "amount_of_upvotes", instance.amount_of_upvotes
        )
        instance.save()
        return instance
