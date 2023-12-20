from .models import Comment, Technique
from .filters import PostFilter
from django import forms


class CommentForm(forms.ModelForm):
    """ Form to add a comment """
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(
                attrs={'rows':3, 'placeholder': 'Add a comment'}),
        }

        labels = {
            'body': 'Comment below:'
        }


class TechniqueForm(forms.ModelForm):
    """ Form to create a Technique """
    class Meta:
        model = Technique
        fields = ['title', 'vid_url', 'description', 'thumbnail','thumbnail_alt_text', 'status', 'keywords']

        widgets = {
            'description': forms.Textarea(attrs={'rows':5}),
        }

        labels = {
            'vid_url': 'Video URL: must be embed src link from Youtube',
            'thumbnail_alt_text': 'Thumbnail alt text'
        }
        