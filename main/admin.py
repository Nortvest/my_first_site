from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'photo', 'time_create', 'time_update', 'is_posted', 'topic_id')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-title', )


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Topic, TopicAdmin)
