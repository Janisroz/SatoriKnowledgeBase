from django.shortcuts import render
from django.views import generic
from .models import Post, Keyword
from .forms import VideoFilterForm


class VideoList(generic.ListView):
    posts = Post
    keywords = Keyword
    queryset = Post.objects.filter(status=1).order_by('-upload_date')
    template_name = 'index.html'
    paginate_by = 8
