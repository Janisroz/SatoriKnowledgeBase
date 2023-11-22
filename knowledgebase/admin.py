from django.contrib import admin
from .models import Post, Keyword, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'keywords__name']
    list_display = ('title', 'status', 'upload_date')
    list_filter = ('status', 'upload_date', 'keywords')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'approved', 'created_on')
    list_filter = ('approved', 'post', 'created_on')
    search_fields = ['post', 'title', 'body', 'email']
    acions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name',)
