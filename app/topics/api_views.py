from rest_framework import generics
from .models import Topic
from .serializers import TopicListSerializer
from django.db.models import Max


class TopicList(generics.ListCreateAPIView):
    # queryset = Topic.objects.all()
    serializer_class = TopicListSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        cat = self.request.GET.get('filter')
        # object_list = Topic.objects.filter(title__icontains=search)
        object_list = Topic.objects.annotate(number_replies=Max('response'))
        if search is not None:
            object_list = object_list.filter(title__icontains=search)
        if cat == '1':
            object_list = object_list.filter(solved=True)
        if cat == '2':
            object_list = object_list.filter(solved=False)
        if cat == '3':
            object_list = object_list.filter(number_replies=None)
        return object_list

    # queryset = get_queryset()
