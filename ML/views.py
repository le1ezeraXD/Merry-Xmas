from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ML.forms import TopicForm
from ML.models import Topic


# Create your views here.
def index(request):
    return render(request, 'ML/index.html')

def base(requeset):
    return render(requeset, 'ML/base.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'ML/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'ML/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ML:topics'))
    context = {'form': form}
    return render(request, 'ML/new_topic.html', context)