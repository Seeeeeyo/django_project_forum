from rest_framework import generics, viewsets, status
from rest_framework.response import Response as resp

from .models import Topic, Response
from .serializers import TopicListSerializer, TopicDetailSerializer, ResponseSerializer
from django.db.models import Max


class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicListSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['author'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return resp(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        search = self.request.GET.get('search')
        cat = self.request.GET.get('filter')
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


class TopicDetail(generics.RetrieveAPIView):
    serializer_class = TopicDetailSerializer
    queryset = Topic.objects.all()

class ResponseCreate(generics.CreateAPIView):
    serializer_class = ResponseSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['author'] = request.user.pk
        data['topic'] = kwargs['pk']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return resp(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
