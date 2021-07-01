from rest_framework import generics
from .models import Topic
from .serializers import TopicDetailSerializer


class TopicDetail(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
