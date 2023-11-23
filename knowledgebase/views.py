from django.shortcuts import render
from django.views import generic
from .models impor Post 

class VideoList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-upload_date')
    template_name = 'index.html'
    paginate_by = 8


