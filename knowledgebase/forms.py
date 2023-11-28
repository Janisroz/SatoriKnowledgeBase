from .models import Keyword, Post
from django import forms
import django_filters


class VideoTitleForm(forms.Form):
    title = forms.CharField() 
    
