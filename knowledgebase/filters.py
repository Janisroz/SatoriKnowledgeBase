import django_filters
from .models import Post, Keyword
from django.db import models
from django import forms
from django.forms import TextInput


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Title:',
        widget=TextInput(
            attrs={

                'class': 'form-select form-select-sm'}

        )
    )

    keywords = django_filters.ModelMultipleChoiceFilter(
        queryset=Keyword.objects.all(),
        label='Keywords:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select form-select-sm'}
        )
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'keywords'
        ]
