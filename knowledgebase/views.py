from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Keyword
from .forms import VideoTitleForm
from .filters import PostFilter
from django.views.generic.list import ListView


# class VideoList(generic.ListView):
#     posts = Post
#     keywords = Keyword
#     queryset = Post.objects.filter(status=1).order_by('-upload_date')
#     template_name = 'index.html'
#     paginate_by = 8
#     form: VideoTitleForm()


def index(request):
    title = request.GET.get('title')
    posts = Post.objects.all()
    if title:
        posts = posts.filter(title__icontains=title)
    # post_filter = PostFilter(request.GET, queryset=Post.objects.all())
    context = {
        'form': VideoTitleForm(),
        'post_list': posts
    }
    return render(request, 'index.html', context)


# class VideoList(ListView):
#     queryset = Post.objects.filter(status=1).order_by('-upload_date')
#     template_name = 'index.html'
#     context_object_name = 'post_list'
#     paginate_by = 8

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = PostFilter(self.request.GET, queryset=queryset)
#         return self.filterset.qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.filterset.form
#         return context
