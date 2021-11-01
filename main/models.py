from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_posted = models.BooleanField(default=False, verbose_name='Опубликовано')
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, verbose_name='Тема')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_post', kwargs={'topic': Topic.objects.filter(pk=self.topic_id)[0].slug,
                                            'post': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-title', 'content']


class Topic(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название темы')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news_topic', kwargs={'topic': self.slug})

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
