from django.urls import path, include

import topics.views

urlpatterns = [
    path('', topics.views.TopicListTemplateView.as_view(), name='topic_list'),
    path('<int:pk>/', topics.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    path('new/', topics.views.TopicCreateTemplateView.as_view(), name='topic_create'),
    path('response/<int:topic_id>', topics.views.response, name='response'),
]