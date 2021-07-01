from rest_framework import serializers
from .models import Topic
from user.serializers import AuthorSerializer

class TopicLastMessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='get_last_message_author')
    date = serializers.CharField(source='get_last_message_date')

    class Meta:
        model = Topic
        fields = ['author', 'date']

class TopicDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    last_message = TopicLastMessageSerializer(source='*')

    count_replies = serializers.CharField(source='get_replies_count')

    class Meta:
        model = Topic
        fields = ['id', 'title', 'date', 'text', 'solved', 'count_replies', 'author', 'last_message']
        depth = 1


    def create(self, validated_data):
        """
        Create and return a new `Topic` instance, given the validated data.
        """
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Topic` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.text = validated_data.get('text', instance.text)
        instance.solved = validated_data.get('solved', instance.solved)
        instance.author = validated_data.get('author', instance.author)
        instance.author_avatar = validated_data.get('author_avatar', instance.author_avatar)
        instance.number_replies = validated_data.get('number_replies', instance.number_replies)
        instance.save()
        return instance

# nombre de topics en tout
# url du prochain topic et du precedent topic
# liste de resultats: id, titre, description, nombre, solved, when, creator serializer, qui est le dernier a repondre (author) et quand
