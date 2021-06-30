from django import template
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Topic, Response
from django.db.models import Max
from django.utils import timezone
from django.shortcuts import HttpResponseRedirect, get_object_or_404


class TopicListTemplateView(ListView):
    template_name = 'topics/topic_list.html'
    model = Topic
    paginate_by = 3

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


class TopicDetailTemplateView(DetailView):
    template_name = 'topics/topic_detail.html'
    model = Topic


def response(request, topic_id):
    if request.user.is_authenticated:
        topic = get_object_or_404(Topic, pk=topic_id)
        topic.response_set.create(text=request.POST.get('text'), date=timezone.now(), author=request.user)
    return HttpResponseRedirect(reverse('topic_detail', args=(topic_id,)))


class TopicCreateTemplateView(CreateView):
    template_name = 'topics/topic_create.html'
    model = Topic
    fields = ['title', 'text']
    success_url = {}

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date = timezone.now()
        self.object.author = self.request.user
        self.object.save()
        # print(request.user.is_authenticated)
        return HttpResponseRedirect(reverse('topic_detail', args=(self.object.id,)))
