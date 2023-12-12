from .models import Comment, Technique
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class TechniqueForm(forms.ModelForm):
    """ Form to create a Technique """
    class Meta:
        model = Technique
        fields = ['title', 'slug', 'vid_url', 'description', 'thumbnail', 'status', 'keywords']

        widget = {
            'description': forms.Textarea(attrs={'rows':5}),
        }

        labels = {
            'vid_url': 'Video URL'
        }