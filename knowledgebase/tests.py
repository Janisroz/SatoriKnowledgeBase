from django.test import TestCase
from .forms import CommentForm,TechniqueForm
from .models import Technique, Keyword, STATUS, Comment
from .views import VideoPost


class TestCommentForm(TestCase):
    """ Test Comment Form """
    def test_comment_form_is_valid(self):
        """ Test comment form is valid """
        comment_form = CommentForm({
            'body': 'Test Form'
        })
        self.assertTrue(comment_form.is_valid())

    def test_comment_form_is_invalid(self):
        """ Test comment form is invalid """
        comment_form = CommentForm({
            'body': ''
        })
        self.assertFalse(comment_form.is_valid())

class TestTechniqueForm(TestCase):
    """ TestTechniqueForm """
    def setUp(self):
        """ Create a Keyword for testing """
        self.keyword = Keyword.objects.create(name='Test Keyword')
        
    def test_technique_form_is_valid(self):
        """ Test Technique form is valid """
        technique_form = TechniqueForm({
           'title': 'Test Technique',
            'slug': 'test-technique',
            'vid_url': 'https://www.example.com/video.mp4',
            'description': 'This is a test technique description.',
            'thumbnail': 'https://www.example.com/thumbnail.jpg',
            'status': STATUS[1][0],  # Use the second status choice (Published)
            'keywords': [self.keyword.id],  # Pass the keyword ID as a list
        })
        self.assertTrue(technique_form.is_valid())
    
    def test_invalid_technique_form_empty_fields(self):
        """ Test Technique form is invalid """
        # Test the form with empty required fields
        data = {
            # All required fields are empty
        }
        form = TechniqueForm(data=data)
        self.assertFalse(form.is_valid())

        # Check individual fields for errors
        self.assertIn('title', form.errors)
        self.assertIn('slug', form.errors)
        self.assertIn('vid_url', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('thumbnail', form.errors)
        self.assertIn('status', form.errors)
        self.assertIn('keywords', form.errors)
    
    def test_invalid_form_partial_empty_fields(self):
        """ Test the form with some required fields empty """
        data = {
            'title': 'Test Technique',
            'slug': 'test-technique',
            'vid_url': '',  # Empty video URL
            'description': 'This is a test technique description.',
            'thumbnail': '',  # Empty thumbnail URL
            'status': '',  # Empty status
            'keywords': [],  # Empty list for keywords
        }

        form = TechniqueForm(data=data)
        self.assertFalse(form.is_valid())

        # Check individual fields for errors
        self.assertNotIn('title', form.errors)
        self.assertNotIn('slug', form.errors)
        self.assertIn('vid_url', form.errors)
        self.assertNotIn('description', form.errors)
        self.assertIn('thumbnail', form.errors)
        self.assertIn('status', form.errors)
        self.assertIn('keywords', form.errors)

    
class TestTechniqueView(TestCase):
    
    def setUp(self):
        """ Create a SuperUser for testing """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        """ Create a Keyword for testing """
        self.keyword = Keyword.objects.create(name='Test Keyword')

        """ Create a Technique for testing """
        self.technique = Technique.objects.create(
            title= 'Test Technique',
            slug= 'test-technique',
            vid_url= 'https://www.example.com/video.mp4',
            description= 'This is a test technique description.',
            thumbnail= 'https://www.example.com/thumbnail.jpg',
            status= STATUS[1][0],  # Use the second status choice (Published)
        )

        self.technique.keywords.set([self.keyword.id]) # add the keyword ID to the technique

        """ Create a Comment for testing """
        self.comment = Comment.objects.create(
            name='myUsername',
            body='This is a test comment.',
            technique=self.technique,
            approved=True
        )

