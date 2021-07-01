from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

import topics.api_views

urlpatterns = [
    path('', topics.views.TopicListTemplateView.as_view(), name='topic_list'),
    path('<int:pk>/', topics.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    path('new/', topics.views.TopicCreateTemplateView.as_view(), name='topic_create'),
    path('react/', topics.views.ReactTemplateView.as_view(), name='topic_react'),
    path('response/<int:topic_id>', topics.views.response, name='response'),
    path('topics/<int:pk>/', topics.api_views.TopicDetail.as_view(), name='topic_detail'),
]