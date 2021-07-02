from rest_framework import serializers
from .models import Topic, Response
# from user.serializers import AuthorSerializer


class TopicLastMessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='get_last_message_author', read_only=True)
    date = serializers.CharField(source='get_last_message_date', read_only=True)

    class Meta:
        model = Topic
        fields = ['author', 'date']


class TopicListSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=False)
    date = serializers.DateTimeField(read_only=True)

    last_message = TopicLastMessageSerializer(source='*', read_only=True)

    count_replies = serializers.CharField(source='get_replies_count', read_only=True)

    def is_valid(self, raise_exception=False):
        print(self.initial_data)
        serializers.BaseSerializer.is_valid(self, raise_exception)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'date', 'text', 'solved', 'count_replies', 'author', 'last_message']
        depth = 1

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Topic` instance, given the validated data.
    #     """
    #     return Topic.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Topic` instance, given the validated data.
    #     """
    #     instance.id = validated_data.get('id', instance.title)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.count_replies = validated_data.get('count_replies', instance.count_replies)
    #     instance.solved = validated_data.get('solved', instance.solved)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.last_message_author = validated_data.get('last_message_author', instance.last_message_author)
    #     instance.last_message_date = validated_data.get('number_replies', instance.last_message_date)
    #     instance.save()
    #     return instance


class ResponseSerializer(serializers.ModelSerializer):
    # avatar_url = serializers.CharField(source='get_avatar', required=False)
    # author_name = serializers.CharField(source='get_author', required=False)

    class Meta:
        model = Response
        fields = ['text', 'author', 'topic']


class TopicDetailSerializer(serializers.ModelSerializer):
    # response = ResponseSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'text', 'date', 'solved', 'author', 'response_set']
        depth = 1
