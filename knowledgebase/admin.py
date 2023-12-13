from django.contrib import admin
from .models import Technique, Keyword, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Technique)
class PostAdmin(SummernoteModelAdmin):
    """ Technique Admin Panel Control """
    search_fields = ['title', 'keywords__name']
    list_display = ('title', 'status', 'upload_date')
    list_filter = ('status', 'upload_date', 'keywords')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Comment Admin Panel Control """
    list_display = ('technique', 'approved', 'created_on')
    list_filter = ('approved', 'technique', 'created_on')
    search_fields = ['post', 'title', 'body', 'email']
    acions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Keyword)
""" Keyword Admin Panel Control """
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name',)
