from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Keyword(models.Model):
    """ Model to create Keyword """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Technique(models.Model):
    """ Model to create Technique """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    vid_url = models.URLField(max_length=200)
    description = models.CharField(max_length=300)
    thumbnail = ResizedImageField(
        size=[205, None],
        quality=75,
        upload_to="thumbnails/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    thumbnail_alt_text = models.CharField(max_length=200, blank=True)
    upload_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    keywords = models.ManyToManyField(Keyword)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """ Model to create Comment """
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=300)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
