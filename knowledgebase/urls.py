from . import views
from django.urls import path

urlpatterns = [
    path('', views.VideoList.as_view(), name='index'),
    path('<slug:slug>', views.video_post.as_view(), name='video_post'),
    path('like/<slug:slug>', views.LikedPost.as_view(), name='LikedPost'),
]
