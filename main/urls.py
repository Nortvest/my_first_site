from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news', news, name='news'),
    path('news/<slug:topic>', news_topic, name='news_topic'),
    path('news/<slug:topic>/<slug:post>', news_post, name='news_post'),
    path('info', info, name='info'),
    path('about', about, name='about')
]
