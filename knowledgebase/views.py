from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Technique, Keyword
from .filters import PostFilter
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .forms import CommentForm, TechniqueForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class VideoList(ListView):
    """ Technique List View"""
    queryset = Technique.objects.filter(status=1).order_by('-upload_date')
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


class VideoPost(View):
    """ View Technique View"""
    def get(self, request, slug, *args, **kwargs):
        queryset = Technique.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "video_post.html",
            {
                "post": post,
                "comments": comments,
                "commented":False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Technique.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.technique = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "video_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            }
        )

class LikedPost(View):
    """ Add and Remove Likes View"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Technique, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('video_post', args=[slug]))

class CreateTechnique(LoginRequiredMixin, CreateView):
    """Create Technique View"""
    template_name = 'add_technique.html'
    model = Technique
    form_class = TechniqueForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTechnique, self).form_valid(form)

class EditTechnique(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Technique"""
    template_name='knowledgebase/edit_technique.html'
    form_class = TechniqueForm
    model = Technique
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser

class DeleteTechnique(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a Technique """
    model=Technique
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser


class LikedTechniques(LoginRequiredMixin, View):
    """" View Users Liked Techniques """
    template_name = 'knowledgebase/liked_techniques.html'
    paginate_by = 9

    def get(self, request, *args, **kwargs):
        # Retrieve the liked techniques for the logged-in user
        liked_techniques = Technique.objects.filter(likes=request.user)

        context = {
            'liked_techniques': liked_techniques
        }

        return render(request, self.template_name, context)
