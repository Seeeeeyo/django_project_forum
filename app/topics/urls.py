from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

import topics.api_views
import topics.views

# router = DefaultRouter()
# router.register(r'topics', topics.api_views.TopicDetail)

urlpatterns = [
    path('', topics.views.TopicListTemplateView.as_view(), name='topic_list'),
    path('<int:pk>/', topics.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    path('new/', topics.views.TopicCreateTemplateView.as_view(), name='topic_create'),
    path('react/', topics.views.ReactTemplateView.as_view(), name='topic_react'),
    path('response/<int:topic_id>', topics.views.response, name='response'),
    path('topics/', topics.api_views.TopicList.as_view(), name='topic_api_list'),
    path('topics/<int:pk>/', topics.api_views.TopicDetail.as_view(), name='topic_api_detail'),
    path('topics/<int:pk>/respond', topics.api_views.ResponseCreate.as_view(), name='topic_api_response'),
    # path('', include(router.urls))
]