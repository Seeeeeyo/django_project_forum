from rest_framework import generics
from .models import Topic
from .serializers import TopicListSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer
