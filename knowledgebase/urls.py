from . import views
from django.urls import path

urlpatterns = [
    path('', views.VideoList.as_view(), name='index'),
    path('<slug:slug>', views.VideoPost.as_view(), name='video_post'),
    path('like/<slug:slug>', views.LikedPost.as_view(), name='LikedPost'),
    path('video_post/', views.createTechnique.as_view(), name='video_post'),
    path('delete/<slug:slug>/', views.DeleteTechnique.as_view(), name='delete_technique'),
]
