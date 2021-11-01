from django.shortcuts import render, get_object_or_404
from .models import News, Topic
from loguru import logger


def index(request):
    return render(request, 'main/index.html', {'title': 'Home'})


def news(request):
    return render(request, 'main/news.html', {'title': 'News',
                                              'active': 0,
                                              'news': News.objects.all(),
                                              'menu': Topic.objects.all()})


def news_topic(request, topic):
    topic_row = get_object_or_404(Topic, slug=topic)
    return render(request, 'main/news.html', {'title': 'News',
                                              'title_h1': topic_row.name,
                                              'active': topic_row.pk,
                                              'news': News.objects.filter(topic_id=topic_row.pk),
                                              'menu': Topic.objects.all()})


def news_post(request, topic, post):
    post = News.objects.filter(slug=post, topic_id=Topic.objects.filter(slug=topic)[0].pk)[0]
    return render(request, 'main/post.html', {'title': post.title, 'post': post})


def info(request):
    return render(request, 'main/info.html', {'title': 'Info'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
