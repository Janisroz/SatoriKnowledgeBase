from .models import Keyword, Post
from django import forms
import django_filters


class VideoTitleForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title')


class KeywordFilter(django_filters.FilterSet):
    
