from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Keyword
from .filters import PostFilter
from django.views.generic.list import ListView


class VideoList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-upload_date')
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
